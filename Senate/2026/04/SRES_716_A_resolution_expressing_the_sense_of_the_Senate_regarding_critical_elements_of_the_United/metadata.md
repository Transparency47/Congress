# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/716?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/716
- Title: A resolution expressing the sense of the Senate regarding critical elements of the United States policy towards the People's Republic of China.
- Congress: 119
- Bill type: SRES
- Bill number: 716
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-14T10:56:29Z
- Update date including text: 2026-05-14T10:56:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2178-2179)
- 2026-04-30 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-30: Submitted in Senate

## Actions

- 2026-04-30 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2178-2179)
- 2026-04-30 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/716",
    "number": "716",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "A resolution expressing the sense of the Senate regarding critical elements of the United States policy towards the People's Republic of China.",
    "type": "SRES",
    "updateDate": "2026-05-14T10:56:29Z",
    "updateDateIncludingText": "2026-05-14T10:56:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S2178-2179)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-04-30T19:15:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NH"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "VA"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "OH"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "WA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "UT"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NJ"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "IN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NC"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "IN"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "MS"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres716is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 716\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Coons (for himself, Mr. Ricketts , Mrs. Shaheen , Mr. Cruz , Mr. Kaine , Mr. Moreno , Mrs. Murray , Mr. Curtis , Mr. Kim , Mr. McCormick , Ms. Duckworth , Mr. Banks , Mr. Tillis , Mr. Young , Mr. Wicker , and Ms. Slotkin ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate regarding critical elements of the United States policy towards the People's Republic of China.\nThat it is the sense of the Senate that the United States should\u2014\n**(1)**\naddress the security, economic, technological, diplomatic, and strategic threats posed by the People's Republic of China as the foremost priorities of United States foreign policy;\n**(2)**\nsustain and strengthen deterrence against the People's Republic of China and enhance the capacity of the United States\u2014\n**(A)**\nto defend its interests;\n**(B)**\nto support freedom of navigation; and\n**(C)**\nto maintain peace and stability in the Indo-Pacific region, including in the Taiwan Strait and the South China Sea;\n**(3)**\nprotect United States economic interests against the predatory economic and trade practices of the People's Republic of China, including by\u2014\n**(A)**\nstrengthening export controls and closing loopholes;\n**(B)**\nrestricting investments in strategic industries in the United States;\n**(C)**\nenforcing forced labor restrictions; and\n**(D)**\nimposing costs to offset state-subsidized entities and goods;\n**(4)**\ndominate the artificial intelligence and other foundational technologies sectors compared to the People's Republic of China and other peer and near-peer competitors;\n**(5)**\nreaffirm the ironclad United States commitment to, and support for, United States treaty allies in the Indo-Pacific region, which stand at the frontlines of the People's Republic of China\u2019s aggression, increased defense spending to deter such aggression, and provide vital basing for United States forces, including\u2014\n**(A)**\nJapan, consistent with the Treaty of Mutual Cooperation and Security Between the United States of America and Japan, signed at Washington, January 19, 1960;\n**(B)**\nSouth Korea, consistent with the Mutual Defense Treaty Between the United States and the Republic of Korea, signed at Washington, October 1, 1953;\n**(C)**\nAustralia, consistent with the Security Treaty between Australia, New Zealand, and the United States of America, signed at San Francisco, September, 1951, and through the partnership among Australia, the United Kingdom, and United States (commonly known as AUKUS );\n**(D)**\nthe Philippines, consistent with the Mutual Defense Treaty between the United States and the Philippines, signed at Washington, August 30, 1951; and\n**(E)**\ntrilateral cooperation between United States allies in the Indo-Pacific region, including among\u2014\n**(i)**\nthe United States, Japan, and South Korea;\n**(ii)**\nthe United States, Japan, and the Philippines; and\n**(iii)**\nthe United States, Japan, and Australia;\n**(6)**\npreserve peace and stability across the Taiwan Strait and maintain the longstanding United States policy on Taiwan, guided by the Taiwan Relations Act of 1979 ( Public Law 96\u20138 ; 22 U.S.C. 3301 et seq. ), the Three Joint Communiqu\u00e9s between the United States and the People's Republic of China, and the Six Assurances between the United States and Taiwan;\n**(7)**\nstrengthen support for United States partners in the Indo-Pacific region, including partners facing military, economic, and gray-zone coercion from the People\u2019s Republic of China, including by\u2014\n**(A)**\nbroadening United States engagement with India, including through the Quadrilateral Security Dialogue;\n**(B)**\nadvancing United States partnerships with countries comprising the Association of Southeast Asian Nations; and\n**(C)**\nworking with Pacific island countries to support their resilience and prosperity;\n**(8)**\nmitigate the leadership and influence of the People's Republic of China in multilateral organizations, technical bodies, and international standards-setting institutions to prevent the adoption of rules or standards that disadvantage the interests of the United States or of its partners; and\n**(9)**\nadvance the democratic norms and values that promote human rights, openness, and the flourishing of civil society in the Indo-Pacific region and beyond, in accordance with United States laws, such as Public Law 117\u201378 (commonly referred to as the Uyghur Forced Labor Prevention Act ) and the Asia Reassurance Initiative Act of 2018 ( Public Law 115\u2013409 ; 22 U.S.C. 3301 note).",
      "versionDate": "2026-04-30",
      "versionType": "IS"
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
        "updateDate": "2026-05-06T20:47:27Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres716is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing the sense of the Senate regarding critical elements of the United States policy towards the People's Republic of China.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T05:18:24Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate regarding critical elements of the United States policy towards the People's Republic of China.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T10:56:28Z"
    }
  ]
}
```
