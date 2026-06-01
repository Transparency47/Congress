# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5838?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5838
- Title: Combatting the Persecution of Religious Groups in China Act
- Congress: 119
- Bill type: HR
- Bill number: 5838
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2025-12-05T22:07:04Z
- Update date including text: 2025-12-05T22:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-28 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-28 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5838",
    "number": "5838",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "A000379",
        "district": "4",
        "firstName": "Mark",
        "fullName": "Rep. Alford, Mark [R-MO-4]",
        "lastName": "Alford",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Combatting the Persecution of Religious Groups in China Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:07:04Z",
    "updateDateIncludingText": "2025-12-05T22:07:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-10-28T17:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-28T17:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "FL"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "MI"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "CO"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5838ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5838\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Mr. Alford (for himself, Mr. Steube , Mr. Crenshaw , and Mr. McCaul ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo state the policy of the United States with respect to religious freedom in the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Combatting the Persecution of Religious Groups in China Act .\n#### 2. Statement of policy\n##### (a) Holding officials of the People\u2019s Republic of China responsible for religious freedom abuses\nIt is the policy of the United States to consider that any official of the Government of the People\u2019s Republic of China who is responsible for or has directly carried out abuses of religious freedom, including those involving arbitrary detention, forced sterilization, torture, forced labor, and serious restrictions on freedom of religion or belief, expression, and movement against religious minorities, including Protestant Christians, Catholics, Buddhists, Muslims, and Falun Gong practitioners, in the People\u2019s Republic of China may have committed a gross violation of internationally recognized human rights for purposes of imposing sanctions with respect to such official under the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 10101 et seq. ).\n##### (b) Department of State programming To promote religious freedom in the People\u2019s Republic of China\nIt is the policy of the United States\u2014\n**(1)**\nthat the relevant bureaus of the Department of State, including the Bureau of East Asian and Pacific Affairs, should support efforts to promote international religious freedom in the People\u2019s Republic of China; and\n**(2)**\nfor programs of the Department of State to promote religious freedom in the People\u2019s Republic of China and monitor transnational repression of religious minority groups engaged in by the Government of the People\u2019s Republic of China.\n#### 3. Sense of Congress regarding promotion of religious freedom in the People\u2019s Republic of China\nIt is the sense of Congress that the United States should promote religious freedom in the People\u2019s Republic of China by\u2014\n**(1)**\ndesignating the People\u2019s Republic of China as a country of particular concern for religious freedom under section 402(b)(1)(A)(ii) of the International Religious Freedom Act of 1998 ( 22 U.S.C. 6442(b)(1)(A)(ii) ) as long as the Government of the People\u2019s Republic of China continues to engage in particularly severe violations of religious freedom (as defined in section 3 of such Act ( 22 U.S.C. 6402 ));\n**(2)**\nstrengthening diplomacy relating to religious freedom on behalf of Christians and other religious minorities facing restrictions in the People\u2019s Republic of China, including through the widespread engagement of international partners to combat abuses of religious freedom committed by the Government of the People\u2019s Republic of China;\n**(3)**\nraising the cases of religious and political prisoners at the highest levels with officials of the People\u2019s Republic of China;\n**(4)**\ncalling on the Government of the People\u2019s Republic of China to unconditionally release all unjustly detained religious and political prisoners and ensure that detainees who have not yet been released are treated humanely with\u2014\n**(A)**\naccess to family, the legal counsel of their choice, independent medical care, and international monitoring mechanisms; and\n**(B)**\nthe ability to practice their faith while in detention; and\n**(5)**\nencouraging the global faith community to speak in solidarity with oppressed religious groups in the People\u2019s Republic of China.",
      "versionDate": "2025-10-28",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-27",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "3056",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Combatting the Persecution of Religious Groups in China Act",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-11-19T17:28:37Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5838ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Combatting the Persecution of Religious Groups in China Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combatting the Persecution of Religious Groups in China Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T09:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To state the policy of the United States with respect to religious freedom in the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:03:18Z"
    }
  ]
}
```
