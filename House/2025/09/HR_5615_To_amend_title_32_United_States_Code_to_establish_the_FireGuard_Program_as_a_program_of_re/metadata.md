# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5615?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5615
- Title: To amend title 32, United States Code, to establish the FireGuard Program as a program of record of the National Guard.
- Congress: 119
- Bill type: HR
- Bill number: 5615
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-12-16T17:23:06Z
- Update date including text: 2025-12-16T17:23:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5615",
    "number": "5615",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000830",
        "district": "27",
        "firstName": "George",
        "fullName": "Rep. Whitesides, George [D-CA-27]",
        "lastName": "Whitesides",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To amend title 32, United States Code, to establish the FireGuard Program as a program of record of the National Guard.",
    "type": "HR",
    "updateDate": "2025-12-16T17:23:06Z",
    "updateDateIncludingText": "2025-12-16T17:23:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
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
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:00:10Z",
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
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "CO"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5615ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5615\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Whitesides (for himself, Mr. Crank , Mr. Carbajal , Mr. Garamendi , and Mr. Crow ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 32, United States Code, to establish the FireGuard Program as a program of record of the National Guard.\n#### 1. FireGuard Program: program of record; authorization\n##### (a) In general\nSection 510 of title 32, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking may and inserting shall ;\n**(B)**\nby inserting of record after carry out a program ; and\n**(C)**\nby striking Such a program and inserting Such program ; and\n**(2)**\nby adding at the end the following new subsections:\n(c) Annual briefing Not later than one year after the date of the enactment of the National Defense Authorization Act for Fiscal Year 2026, the Secretary shall submit to the Committees on Armed Services of the Senate and House of Representatives the first of five annual briefings regarding the FireGuard Program. Such a briefing shall include, with regards to the year preceding the date of the briefing, the following elements: (1) The States (as such term is defined in section 901 of this title), counties, municipalities, and Tribal governments that received information under the FireGuard Program. (2) A comparative analysis of a map of\u2014 (A) each wildfire, initially provided to an entity described in paragraph (1) through the FireGuard Program; and (B) the perimeter of such wildfire after containment. (3) An analysis of the time between the detection of a fire via raw satellite data and alerts being sent to local responders. (4) A review of efforts undertaken to integrate emerging satellite and aerial surveillance technologies from qualified private, nonprofit, and public sector sources. (d) Sunset The FireGuard Program shall terminate on December 31, 2031. .\n##### (b) Clerical amendment\nThe heading of such section is amended by striking Authorization for .",
      "versionDate": "2025-09-26",
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
        "updateDate": "2025-12-16T17:23:06Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5615ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 32, United States Code, to establish the FireGuard Program as a program of record of the National Guard.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T08:18:33Z"
    },
    {
      "title": "To amend title 32, United States Code, to establish the FireGuard Program as a program of record of the National Guard.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T08:05:28Z"
    }
  ]
}
```
