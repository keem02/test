"""
게임 캐릭터 시스템을 만드세요.
- Warrior 클래스: 전사 기본 능력
- Mage 클래스: 마법사 기본 능력
- Paladin 클래스: Warrior와 Mage를 다중상속받는 성기사 클래스

각 클래스는 고유의 능력치와 스킬을 가지며, Paladin은 양쪽의 능력을 모두 사용할 수 있어야 합니다.

테스트 코드:
paladin = Paladin("아서스", 100)
paladin.warrior_attack()
paladin.cast_spell()
paladin.display_info()
"""