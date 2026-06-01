# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8702?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8702
- Title: Secret Service Transfer Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8702
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-21T17:57:35Z
- Update date including text: 2026-05-21T17:57:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8702",
    "number": "8702",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Secret Service Transfer Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T17:57:35Z",
    "updateDateIncludingText": "2026-05-21T17:57:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-07T13:06:25Z",
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
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8702ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8702\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Moskowitz (for himself and Mr. Fry ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish the United States Secret Service within the Executive Office of the President.\n#### 1. Short title\nThis Act may be cited as the Secret Service Transfer Act of 2026 .\n#### 2. Transfer of the United States Secret Service to the Executive Office of the President\n##### (a) Transfer\nThere are hereby transferred to and vested in the Executive Office of the President all functions, personnel, assets, and liabilities of the United States Secret Service (hereinafter in this Act referred to as the Service ), including the officers and components of the Service.\n##### (b) Administrator\nThere shall be at the head of the Service a Director of the Service, who shall be appointed by the President. The Service shall be administered under the supervision and direction of the Director. The Director shall be compensated at the same rate as the Director is compensated at as of the date of enactment of this Act. The Director of the United States Secret Service at the date of enactment of this Act shall continue to serve as the Director of the Service.\n##### (c) Program transfers\nThe functions that, immediately before the effective date of this title, were performed by the Director of the United States Secret Service are hereby transferred. During the transition period, the Secretary of Homeland Security shall provide to the Director such assistance, including the use of personnel and assets, as the Director may request in preparing for the transfer.\n##### (d) Continuation of service\nEach officer and component of the United States Secret Service as of the date of enactment of this Act shall be transferred to the Service and shall continue in operation as part of the Service in the same manner and subject to the same level of compensation and conditions of service.\n##### (e) Reorganization\nThe Director of the United States Secret Service may reorganize the agency as necessary to maximize efficiency, enhance operational effectiveness, and ensure the agency fulfills its protective mission. However, upon transition to the Executive Office of the President, the agency shall initially maintain its organizational structure, roles, and functions as they existed immediately prior to the date of enactment of this Act. Any subsequent reorganization shall comply with applicable Federal laws and regulations.\n##### (f) References\nAny reference in any other Federal law, Executive order, rule, regulation, or delegation of authority, or any document of or pertaining to an agency or office from which a function is transferred by this Act\u2014\n**(1)**\nto the Director of the United States Secret Service or an officer of the United States Secret Service, is deemed to refer to the head of the office, agency, or department to which such function is transferred, and\n**(2)**\nto the United States Secret Service is deemed to refer to the agency or office to which such function is transferred.\n##### (g) Exercise of authorities\nExcept as otherwise provided by law, a Federal official to whom a function is transferred by this Act may, for purposes of performing that function, exercise all authorities under any other provision of law that were available with respect to the performance of that function to the official responsible for the performance of that function immediately before the effective date of the transfer of such function, as provided in this Act.\n##### (h) Transfer of assets, liabilities, and agreements\nIn the case of\u2014\n**(1)**\nany contract or other agreement to which the United States Secret Service is party on the date of enactment of this Act,\n**(2)**\nany asset owned or controlled by the United States Secret Service on the date of enactment of this Act, and\n**(3)**\nany liability of the United States Secret Service on the date of enactment of this Act,\nthe Service shall be considered to be the successor in interest to any such agreement, shall assume any obligations or any such liability, and shall be considered to own or control any such asset.\n##### (i) Finalization date\nAll activities pertaining to the transfer of authorities and functions under this Act shall be finalized by the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2026-05-07",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-21T17:57:35Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8702ih.xml"
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
      "title": "Secret Service Transfer Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secret Service Transfer Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the United States Secret Service within the Executive Office of the President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:18:29Z"
    }
  ]
}
```
