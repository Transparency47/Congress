# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/883?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/883
- Title: Counter SNIPER Act
- Congress: 119
- Bill type: HR
- Bill number: 883
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-09-03T08:05:57Z
- Update date including text: 2025-09-03T08:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/883",
    "number": "883",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Counter SNIPER Act",
    "type": "HR",
    "updateDate": "2025-09-03T08:05:57Z",
    "updateDateIncludingText": "2025-09-03T08:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MS"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr883ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 883\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Pfluger (for himself and Mr. Guest ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the Secretary of Homeland Security to provide candidates with a justification for candidate protection determinations, to require Senate confirmation of the Director of the United States Secret Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Countering Subversion and Negligence in Protecting Election Runners Act or the Counter SNIPER Act .\n#### 2. Presidential candidate protection; Senate confirmation of Director\nSection 3056 of title 18, United States Code, is amended by adding at the end the following:\n(h) (1) In the case that the Secretary of Homeland Security determines that any Presidential or Vice Presidential candidate requesting a protective detail or an increase in assigned protective detail resources is not eligible for such detail or increased resources for the purpose of this section, the Secretary shall submit to the candidate and the advisory committee, within 14 days after such a request is made, a written notice of the Secretary\u2019s determination, indicating the criteria that such candidate failed to meet for such purpose. (2) Any Presidential or Vice Presidential candidate may submit to the Secretary of Homeland Security a written request to reconsider the determination described in paragraph (1), which may include facts to support that the criteria specified by the Secretary of Homeland Security have been met for the purpose of this section. (3) Not later than 14 days after a request for reconsideration is submitted under paragraph (2), the Secretary of Homeland Security shall review such request and submit to the Presidential or Vice Presidential candidate a written notice of the Secretary\u2019s final determination on whether the criteria have been met for the purpose of this section, and provide a copy of such final determination to the advisory committee. (i) The United States Secret Service shall be headed by a Director, who shall be appointed by the President with the advice and consent of the Senate. .",
      "versionDate": "2025-01-31",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Department of Homeland Security",
            "updateDate": "2025-06-20T18:46:31Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-06-20T18:46:27Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-06-20T18:46:19Z"
          },
          {
            "name": "Protection of officials",
            "updateDate": "2025-06-20T18:46:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-02T14:37:58Z"
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
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr883ih.xml"
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
      "title": "Counter SNIPER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Counter SNIPER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Countering Subversion and Negligence in Protecting Election Runners Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Homeland Security to provide candidates with a justification for candidate protection determinations, to require Senate confirmation of the Director of the United States Secret Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:29Z"
    }
  ]
}
```
