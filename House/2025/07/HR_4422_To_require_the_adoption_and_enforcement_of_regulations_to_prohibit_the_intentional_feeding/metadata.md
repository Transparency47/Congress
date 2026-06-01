# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4422?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4422
- Title: Don’t Feed the Bears Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4422
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-03-26T08:06:29Z
- Update date including text: 2026-03-26T08:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-15 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-15 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4422",
    "number": "4422",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "T000488",
        "district": "13",
        "firstName": "Shri",
        "fullName": "Rep. Thanedar, Shri [D-MI-13]",
        "lastName": "Thanedar",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Don\u2019t Feed the Bears Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:29Z",
    "updateDateIncludingText": "2026-03-26T08:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-15T14:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "IN"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "DC"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4422ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4422\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Thanedar (for himself, Mr. Carson , Mr. Krishnamoorthi , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the adoption and enforcement of regulations to prohibit the intentional feeding of bears on Federal public lands in order to end the hunting practice known as bear baiting and reduce the number of dangerous interactions between people and bears.\n#### 1. Short title\nThis Act may be cited as the Don\u2019t Feed the Bears Act of 2025 .\n#### 2. Prohibition on feeding bears on Federal public lands\n##### (a) Findings\nCongress finds the following:\n**(1)**\nFederal land management agencies, including the Forest Service, National Park Service, United States Fish and Wildlife Service, and Bureau of Land Management, publish and distribute materials to the public discouraging any feeding of black bears.\n**(2)**\nEven though Federal land managers are in agreement that private citizens should not provide food to bears, several Federal land management agencies do not prohibit licensed hunters from setting out food as bait for bears on Federal lands in States where baiting is permitted by State law.\n**(3)**\nA typical bait station consists of hundreds of pounds of human-scented foods, often including parts of animal carcasses, pastries, fruits, and grease, that are simply piled on the forest floor or dumped in large drums.\n**(4)**\nThe foods used in a bait station are no different than the human-scented foods that a bear might find in a garbage can, dump, or campground, and after the bear hunting season ends, bait stations are often not removed.\n**(5)**\nThe presence of bait stations on Federal lands allows bears to increase their food intake and results in higher birth rates, increasing bear populations.\n**(6)**\nWildlife scientists agree that black bears are naturally wary of people, but that feeding bears human-scented foods can cause bears to lose their wariness and become emboldened in approaching people and property in search of food.\n**(7)**\nHuman-fed bears cause millions of dollars in property damage every year.\n**(8)**\nBears habituated to human food can pose a safety threat, occasionally resulting in attacks on human beings.\n**(9)**\nBears that come into conflict with people are often labeled as nuisance animals, and are often killed as a means of protecting people and property.\n**(10)**\nWhen the National Park Service adopted policies to ban bear feeding and to end the practice of keeping garbage in open-air dumps, units of the National Park System experienced a dramatic decline in bear-human encounters.\n**(11)**\nA majority of the States that allow bear hunting ban baiting, and black bears can be hunted successfully by means other than baiting.\n**(12)**\nIt is inconsistent for Federal land management agencies to demand that visitors to the Federal lands not feed bears, but to allow this practice by bear baiters.\n**(13)**\nThe United States already prohibits baiting of migratory birds.\n##### (b) Enforcement of existing nps regulation\nThe Secretary of the Interior shall enforce the regulatory prohibition, contained in section 2.2(a)(2) of title 36, Code of Federal Regulations, against the feeding of wildlife on National Park System lands to prohibit individuals from intentionally feeding bears for the purpose of enticing bears to a particular area to be hunted, a practice known as bear baiting .\n##### (c) Enforcement of existing fws regulation\nThe Secretary of the Interior shall enforce the regulatory prohibition, contained in section 32.2(h) of title 50, Code of Federal Regulations, against bear baiting and the baiting of other wildlife on wildlife refuge areas.\n##### (d) Adoption of regulations for other public lands\n**(1) Regulation required**\nThe Secretary of the Interior, with respect to lands administered by the Bureau of Land Management, and the Secretary of Agriculture, with respect to National Forest System lands, shall each adopt and enforce a regulation to prohibit individuals from intentionally feeding bears, including feeding for the purpose of enticing bears to a particular area to be hunted, a practice known as bear baiting .\n**(2) Deadline for adoption**\nThe regulations required by this subsection shall be issued in final form not later than one year after the date of the enactment of this Act.\n##### (e) Exception in extraordinary cases\nThe regulations referred to in subsections (b) and (c), and the regulations required by subsection (d), shall provide an exception in extraordinary cases when the Secretary concerned determines that bear feeding is required for the welfare of the bear, preservation of public safety, or authorized wildlife research.",
      "versionDate": "2025-07-15",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-30T22:40:52Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4422ih.xml"
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
      "title": "Don\u2019t Feed the Bears Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Don\u2019t Feed the Bears Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the adoption and enforcement of regulations to prohibit the intentional feeding of bears on Federal public lands in order to end the hunting practice known as \"bear baiting\" and reduce the number of dangerous interactions between people and bears.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:18:32Z"
    }
  ]
}
```
