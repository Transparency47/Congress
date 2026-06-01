# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2113?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2113
- Title: America Supports Taiwan Act
- Congress: 119
- Bill type: HR
- Bill number: 2113
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-05-15T00:40:07Z
- Update date including text: 2025-05-15T00:40:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2113",
    "number": "2113",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000032",
        "district": "19",
        "firstName": "Byron",
        "fullName": "Rep. Donalds, Byron [R-FL-19]",
        "lastName": "Donalds",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "America Supports Taiwan Act",
    "type": "HR",
    "updateDate": "2025-05-15T00:40:07Z",
    "updateDateIncludingText": "2025-05-15T00:40:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:02:35Z",
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
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "GA"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "WI"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "AL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2113ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2113\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Donalds (for himself, Mr. Collins , Mr. Tiffany , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require agencies to use the term Taiwan instead of Chinese Taipei , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the America Supports Taiwan Act .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds as follows:\n**(1)**\nThe United States Government has never officially recognized the People\u2019s Republic of China\u2019s claim of sovereignty over Taiwan.\n**(2)**\nThe People\u2019s Republic of China, led by the Chinese Communist Party, seeks to control Taiwan through means of persuasion and coercion, and potentially compellence.\n**(3)**\nThe People\u2019s Liberation Army seeks to have the capability to invade Taiwan by 2027, the 100th anniversary of the founding of the Chinese Communist Party\u2019s military, the People\u2019s Liberation Army.\n**(4)**\nThe People\u2019s Republic of China refers to Taiwan as a region and to the President of Taiwan as the leader of the Taiwan region , consistent with its assertion that Taiwan is a region of the People\u2019s Republic of China.\n**(5)**\nTaiwan and mainland China are separated by a median line in the Taiwan Strait, which acts as an unofficial boundary that was generally respected from 1999, until September 2020, when a Chinese Foreign Ministry spokesman stated, there is no so-called median line in the Strait , and People\u2019s Liberation Army aircraft and vessels have repeatedly crossed the median line since then, as more than 1,400 PRC aircraft reportedly crossed the median line in 2024.\n**(6)**\nAn accounting, based on Taiwan Ministry of National Defense reporting, of incursions into Taiwan\u2019s de facto Air Defense Identification Zone by PRC military aircraft illustrates a sharp increase over time, with approximately 3,075 incursions in 2024, up from approximately 390 in 2020, illustrating a more confrontational posture toward Taiwan and honing military capabilities required to conduct combat operations near Taiwan.\n**(7)**\nMany people of Taiwan see the Chinese Taipei nomenclature as a symbol of oppression from the People\u2019s Republic of China, originally stemming from an effort to find a way for both Taiwan and the People\u2019s Republic of China to participate in the 1980 Lake Placid Winter Olympics and the 1980 Moscow Summer Olympics.\n**(8)**\nIn Mandarin Chinese, Taiwan uses a version of Chinese Taipei in which Chinese is the cultural term zhonghua and does not have sovereignty connotations.\n**(9)**\nComparatively, the Chinese-language translation of Chinese Taipei carries the connotation that Taiwan is culturally Chinese, and thus the English term can be easily misunderstood to connote PRC possession of Taipei, and by extension, all of Taiwan.\n##### (b) Purpose\nIt is the sense of Congress that\u2014\n**(1)**\nthe United States must stand firm in the commitments it made in the Taiwan Relations Act ( 22 U.S.C. 3301 et seq. ), which declares that it is the policy of the United States to maintain the capacity of the United States to resist any resort to force or other forms of coercion that would jeopardize the security, or the social or economic system, of the people on Taiwan ;\n**(2)**\nthe United States Government continues to support Taiwan and enable it to maintain a sufficient self-defense capability as it withstands control-seeking persuasion and coercion from an increasingly aggressive People\u2019s Republic of China; and\n**(3)**\nthe United States Government disfavors the use of the Chinese Taipei nomenclature, and instead favors the use of Taiwan so as to avoid connotations of possession with the Chinese Taipei term in English and support resolution of cross-Strait differences by peaceful means, free from coercion, in a manner acceptable to the people on both sides of the Strait.\n#### 3. Agency requirement to use Taiwan\n##### (a) In general\nThe head of an agency may not use Chinese Taipei and shall use Taiwan , except\u2014\n**(1)**\nin historical context explaining the People\u2019s Republic of China\u2019s attempt to control Taiwan through persuasion and coercion; or\n**(2)**\nto the extent that the head of the agency is working on matters relating to Taiwan with an international organization at which Taiwan is a participant under a different official name.\n##### (b) Requirement To update agency websites\nNot later than 14 days after the date of the enactment of this Act, the head of each agency shall ensure the website of the agency meets the requirements of this section.\n##### (c) Agency defined\nThe term agency has the meaning given that term in section 551 of title 5, United States Code.",
      "versionDate": "2025-03-14",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-15T00:40:07Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2113ih.xml"
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
      "title": "America Supports Taiwan Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "America Supports Taiwan Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require agencies to use the term \"Taiwan\" instead of \"Chinese Taipei\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:44Z"
    }
  ]
}
```
