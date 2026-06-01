# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5318?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5318
- Title: RAPID Act
- Congress: 119
- Bill type: HR
- Bill number: 5318
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-24T15:01:27Z
- Update date including text: 2025-09-24T15:01:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5318",
    "number": "5318",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "RAPID Act",
    "type": "HR",
    "updateDate": "2025-09-24T15:01:27Z",
    "updateDateIncludingText": "2025-09-24T15:01:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-11T13:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5318ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5318\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Hudson introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide that the deployment of a small personal wireless service facility is not subject to requirements to prepare certain environmental or historical preservation reviews, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reducing Antiquated Permitting for Infrastructure Deployment Act or the RAPID Act .\n#### 2. Exemptions for small personal wireless service facilities\n##### (a) NEPA exemption\nA Federal authorization with respect to a project to deploy a small personal wireless service facility may not be considered a major Federal action under section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ).\n##### (b) National Historic Preservation Act exemption\nA project to deploy a small personal wireless service facility may not be considered an undertaking under section 300320 of title 54, United States Code.\n#### 3. Presumption with respect to certain complete FCC forms\n##### (a) Presumption\nIf an Indian Tribe is shown to have received a complete FCC Form 620 or FCC Form 621 (or any successor form), or can be reasonably expected to have received a complete FCC Form 620 or FCC Form 621 (or any successor form), and has not acted on a request contained in such complete form by the date that is 45 days after the date of such receipt or reasonably expected receipt\u2014\n**(1)**\nthe Commission and a court of competent jurisdiction (as the case may be) shall presume the applicant with respect to such complete form has made a good faith effort to provide the information reasonably necessary for such Indian Tribe to ascertain whether historic properties of religious or cultural significance to such Indian Tribe may be affected by the undertaking related to such complete form; and\n**(2)**\nsuch Indian Tribe shall be presumed to have disclaimed interest in such undertaking.\n##### (b) Overcoming presumption\n**(1) In general**\nAn Indian Tribe may overcome a presumption under subsection (a) upon making, to the Commission or a court of competent jurisdiction, a favorable demonstration with respect to 1 or more of the factors described in paragraph (2).\n**(2) Factors considered**\nIn making a determination regarding a presumption under subsection (a), the Commission or court of competent jurisdiction shall give substantial weight to\u2014\n**(A)**\nwhether the applicant with respect to the relevant complete form failed to make a reasonable attempt to follow up with the applicable Indian Tribe not earlier than 30 days, and not later than 50 days, after the applicant submitted a complete FCC Form 620 or FCC Form 621 (as the case may be) to such Indian Tribe; and\n**(B)**\nwhether the rules of the Commission, or FCC Form 620 or FCC Form 621, are found to be in violation of a Nationwide Programmatic Agreement of the Commission.\n#### 4. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Communications Commission.\n**(2) Federal authorization**\nThe term Federal authorization \u2014\n**(A)**\nmeans any authorization required under Federal law with respect to a project; and\n**(B)**\nincludes any permits, special use authorizations, certifications, opinions, or other approvals as may be required under Federal law with respect to a project.\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given the term Indian tribe in section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130 ).\n**(4) Personal wireless service**\nThe term personal wireless service \u2014\n**(A)**\nmeans any service described in section 332(c)(7)(C)(i) of the Communications Act of 1934 ( 47 U.S.C. 332(c)(7)(C)(i) ); and\n**(B)**\nincludes commercial mobile data service (as defined in section 6001 of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1401 )).\n**(5) Personal wireless service facility**\nThe term personal wireless service facility means a facility for the provision of personal wireless service.\n**(6) Small personal wireless service facility**\nThe term small personal wireless service facility \u2014\n**(A)**\nmeans a personal wireless service facility with respect to which each antenna is not more than 3 cubic feet in volume; and\n**(B)**\ndoes not include a wireline backhaul facility.\n**(7) Wireline backhaul facility**\nThe term wireline backhaul facility means an above-ground or underground wireline facility used to transport communications service or other electronic communications from a small personal wireless service facility or its adjacent network interface device to a communications network.",
      "versionDate": "2025-09-11",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-24T15:01:27Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5318ih.xml"
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
      "title": "RAPID Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-20T07:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RAPID Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T07:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reducing Antiquated Permitting for Infrastructure Deployment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T07:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that the deployment of a small personal wireless service facility is not subject to requirements to prepare certain environmental or historical preservation reviews, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T07:33:28Z"
    }
  ]
}
```
