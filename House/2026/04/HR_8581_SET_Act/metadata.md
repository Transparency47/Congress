# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8581?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8581
- Title: SET Act
- Congress: 119
- Bill type: HR
- Bill number: 8581
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-16T08:07:31Z
- Update date including text: 2026-05-16T08:07:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-04-29: Introduced in House

## Actions

- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8581",
    "number": "8581",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001245",
        "district": "18",
        "firstName": "Christian",
        "fullName": "Rep. Menefee, Christian D. [D-TX-18]",
        "lastName": "Menefee",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "SET Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:31Z",
    "updateDateIncludingText": "2026-05-16T08:07:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T13:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MD"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-29",
      "state": "DC"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "OH"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "GA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "NJ"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "AL"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8581ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8581\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Mr. Menefee (for himself, Mr. Raskin , Ms. Clarke of New York , Ms. Norton , Mrs. Beatty , and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo require States to hold special elections to fill vacancies in the House of Representatives not later than 180 days after a vacancy occurs in the House of Representatives, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Special Election Timeliness Act or the SET Act .\n#### 2. Requiring special elections to be held to fill vacancies in House\n##### (a) In general\nSection 26(a) of the Revised Statutes of the United States ( 2 U.S.C. 8(a) ) is amended to read as follows:\n(a) In general (1) Special election to fill vacancy Except as provided in subsection (b) and subject to the requirements under paragraph (2), the time for holding elections in any State, District, or Territory for a Representative or Delegate to fill a vacancy, whether such vacancy is caused by a failure to elect at the time prescribed by law, or by the death, resignation, or incapacity of a person elected, may be prescribed by the laws of the several States and Territories respectively. (2) Deadline for special election A special election to fill a vacancy under paragraph (1) shall occur not later than 180 days after the date the vacancy occurs, unless a regularly scheduled general election for the office involved is to be held at any time during the 180-day period which begins on the date the vacancy occurs. (3) Civil enforcement (A) In general The Attorney General may bring a civil action against the chief executive of the State concerned in an appropriate district court for such declaratory or injunctive relief as is necessary to carry out this subsection. (B) Private right of action A person who is aggrieved by a violation of this subsection, including the Speaker of the House of Representatives or the Minority Leader of the House, may bring a civil action against the chief executive of the State concerned in an appropriate district court for such declaratory or injunctive relief as may be necessary to carry out this subsection. (4) Special election defined For purposes of this subsection, the term special election means an election for purposes of electing a candidate to fill a vacancy described in paragraph (1) and does not include an election for purposes of nominating candidates to fill such a vacancy. .",
      "versionDate": "2026-04-29",
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
        "name": "Congress",
        "updateDate": "2026-05-14T15:19:55Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8581ih.xml"
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
      "title": "SET Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T06:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SET Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-01T06:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Special Election Timeliness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-01T06:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require States to hold special elections to fill vacancies in the House of Representatives not later than 180 days after a vacancy occurs in the House of Representatives, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T06:48:27Z"
    }
  ]
}
```
