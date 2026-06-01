# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7952?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7952
- Title: Streamline Upgrades for Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 7952
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-05-13T21:20:47Z
- Update date including text: 2026-05-13T21:20:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7952",
    "number": "7952",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000831",
        "district": "11",
        "firstName": "James",
        "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
        "lastName": "Walkinshaw",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Streamline Upgrades for Veterans Act",
    "type": "HR",
    "updateDate": "2026-05-13T21:20:47Z",
    "updateDateIncludingText": "2026-05-13T21:20:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "GU"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7952ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7952\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. Walkinshaw (for himself and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to prohibit a reduction in the number of personnel assigned to duty with a service review agency, to direct the Secretary of Defense to submit a report regarding consideration of reviews and appeals of discharges or dismissals, based on matters relating to post-traumatic stress disorder or traumatic brain injury, to direct the Secretary of Veterans Affairs to post a summary of such report online, and for other purposes.\n#### 1. Short title\nThis act may be cited as the Streamline Upgrades for Veterans Act .\n#### 2. Prohibition on reduction in the number of personnel assigned to duty with a service review agency\nSection 1559(a) of title 10, United States Code, is amended by striking Before December 31, 2025 and inserting During the period beginning on the date of the enactment of the Streamline Upgrades for Veterans Act and ending on December 31, 2030 .\n#### 3. Report on time required for a board to consider a review of a discharge or dismissal from the Armed Forces based on matters relating to post-traumatic stress disorder or traumatic brain injury\n##### (a) Report required\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense, acting through the Under Secretary of Defense for Personnel and Readiness, in coordination with the Secretaries of the military departments, shall submit to the appropriate congressional committees a report regarding the periods required for a board established under section 1552 or 1553 of title 10, United States Code, to make a determination in a case involving liberal consideration.\n**(2) Elements**\nThe report under paragraph (1) shall include the following:\n**(A)**\nAn analysis of the time of such periods, disaggregated by military department.\n**(B)**\nAn explanation of the differences between such periods, disaggregated by military department.\n**(C)**\nThe number of personnel assigned to review, process, and consider such cases.\n**(D)**\nRecommendations of the Secretary of Defense, which the Secretary may develop in consultation with Federal entities that serve members of the Armed Forces or veterans, to expedite the consideration of such cases.\n**(3) Form**\nThe report shall be submitted in unclassified form.\n**(4) Publication**\nThe executive summary of the report shall be published on a publicly accessible website of\u2014\n**(A)**\nthe Department of Defense; and\n**(B)**\nthe Department of Veterans Affairs.\n##### (b) Briefing\nNot later than 30 days after submitting the report under subsection (a), the Secretary of Defense shall provide to the appropriate congressional committees a briefing on the findings, conclusions, and recommendations of such report.\n##### (c) Definitions\nIn this section:\n**(1)**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services of the House of Representatives;\n**(B)**\nthe Committee on Armed Services of the Senate;\n**(C)**\nthe Committee on Veterans\u2019 Affairs of the House of Representatives; and\n**(D)**\nthe Committee on Veterans\u2019 Affairs of the Senate.\n**(2)**\nThe term liberal consideration is used as such term is used in section 1552(h) and 1553(d) of title 10, United States Code.",
      "versionDate": "2026-03-16",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-13T21:20:47Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7952ih.xml"
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
      "title": "Streamline Upgrades for Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamline Upgrades for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to prohibit a reduction in the number of personnel assigned to duty with a service review agency, to direct the Secretary of Defense to submit a report regarding consideration of reviews and appeals of discharges or dismissals, based on matters relating to post-traumatic stress disorder or traumatic brain injury, to direct the Secretary of Veterans Affairs to post a summary of such report online, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:48:49Z"
    }
  ]
}
```
