# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2476?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2476
- Title: Stop Illegal Campaign Coordination Act
- Congress: 119
- Bill type: HR
- Bill number: 2476
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-05-09T16:12:38Z
- Update date including text: 2025-05-09T16:12:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2476",
    "number": "2476",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Stop Illegal Campaign Coordination Act",
    "type": "HR",
    "updateDate": "2025-05-09T16:12:38Z",
    "updateDateIncludingText": "2025-05-09T16:12:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:06:20Z",
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
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "HI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2476ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2476\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Ms. Tokuda (for herself, Mr. Tonko , Mr. Case , Ms. Jayapal , and Ms. Balint ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to treat expenditures as coordinated with a candidate, an authorized committee of a candidate, or a committee of a national, State, or local political party if the making of the expenditures is materially consistent with instructions, directions, guidance, and suggestions from such candidate or committee, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Illegal Campaign Coordination Act .\n#### 2. Treatment of certain expenditures as coordinated expenditures\n##### (a) In general\nSection 315(a) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30116(a) ) is amended\u2014\n**(1)**\nin paragraph (7)(B)(i), by striking or their agents and inserting or their agents, including expenditures described in paragraph (10), ;\n**(2)**\nin paragraph (7)(B)(ii) by striking political party, and inserting political party, including expenditures described in paragraph (10), ; and\n**(3)**\nby adding at the end the following new paragraph:\n(10) (A) For purposes of paragraph (7)(B)(i) and (ii), an expenditure is described in this paragraph if the making of the expenditure is materially consistent with instructions, directions, guidance, or suggestions from a candidate, an authorized committee of a candidate, or a national, State, or local committee of a political party, or from an agent of any such candidate or committee, regardless of whether the instructions, directions, guidance, or suggestions are made available to the general public or are communicated directly or indirectly to the person making the expenditure. (B) To determine whether the making of an expenditure is materially consistent with instructions, directions, guidance, or suggestions from a candidate or committee for purposes of this paragraph, the Commission shall consider each of the factors described in subparagraph (C), and if the Commission determines that one or more of such factors apply with respect to the making of the expenditure, the making of the expenditure shall be presumed to be materially consistent with instructions, directions, guidance, or suggestions from a candidate or committee for purposes of this paragraph. (C) The factors described in this subparagraph are the following: (i) Whether the instructions, directions, guidance, or suggestions indicate that information regarding a clearly identified candidate or political party should be communicated or disseminated to voters or any subset of voters. (ii) In the case of an expenditure consisting of Federal election activity or a communication which disseminates to any person information about a candidate or political party, whether the instructions, directions, guidance, or suggestions include information regarding the target audience for the communication or the information, such as the demographics, location, or political party affiliation of recipients. (iii) Whether the instructions, directions, guidance, or suggestions include suggested methods of making a communication or disseminating information, such as references to the distribution or receipt of direct mail, audio, video, social media, digital, or other media. (iv) In the case of an expenditure consisting of Federal election activity or a communication which disseminates to any person information about a candidate or political party, whether the instructions, directions, guidance, or suggestions include or are accompanied by any phrase, image, video, or audio is subsequently used, in whole or in part, in communicating or disseminating the information. (v) Whether the instructions, directions, guidance, or suggestions containing one or more other factors identified in this subparagraph are set apart using a signal or cue. (vi) Such other factors as the Commission considers appropriate. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to expenditures made on or after the date of the enactment of this Act.",
      "versionDate": "2025-03-27",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-09T16:12:38Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2476ih.xml"
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
      "title": "Stop Illegal Campaign Coordination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Illegal Campaign Coordination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to treat expenditures as coordinated with a candidate, an authorized committee of a candidate, or a committee of a national, State, or local political party if the making of the expenditures is materially consistent with instructions, directions, guidance, and suggestions from such candidate or committee, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:32Z"
    }
  ]
}
```
