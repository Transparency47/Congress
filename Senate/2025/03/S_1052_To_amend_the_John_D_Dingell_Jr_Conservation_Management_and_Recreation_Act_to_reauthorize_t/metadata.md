# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1052?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1052
- Title: A bill to amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to reauthorize the National Volcano Early Warning and Monitoring System, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 1052
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1052",
    "number": "1052",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "A bill to amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to reauthorize the National Volcano Early Warning and Monitoring System, and for other purposes.",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-03-13T19:56:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "WA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "HI"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1052is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1052\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Ms. Murkowski (for herself, Ms. Cantwell , Ms. Hirono , and Mr. Sullivan ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to reauthorize the National Volcano Early Warning and Monitoring System, and for other purposes.\n#### 1. Reauthorization of the National Volcano Early Warning and Monitoring System\n##### (a) Modernization activities\nSection 5001(b)(2)(B) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( 43 U.S.C. 31k(b)(2)(B) ) is amended\u2014\n**(1)**\nby striking the System shall include the comprehensive application and inserting the following: \u201cthe System shall include\u2014\n(i) the comprehensive application ;\n**(2)**\nin clause (i) (as so designated)\u2014\n**(A)**\nby striking Global Positioning System and inserting Global Navigation Satellite System ;\n**(B)**\nby striking and unoccupied aerial vehicles and inserting unoccupied aerial vehicles, infrasound arrays, visible and infrared cameras, and advanced digital telemetry networks ; and\n**(C)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(ii) maintaining or expanding the technical instrumentation and infrastructure required for the comprehensive application of the emerging technologies described in clause (i), particularly advanced digital telemetry networks. .\n##### (b) Management plan\nSection 5001(b)(3)(A) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( 43 U.S.C. 31k(b)(3)(A) ) is amended\u2014\n**(1)**\nin clause (ii)(III), by inserting (including new or existing cooperative agreements) after partnerships ; and\n**(2)**\nin clause (iii)\u2014\n**(A)**\nin the clause heading, by striking Update and inserting Updates ; and\n**(B)**\nin subclause (II)\u2014\n**(i)**\nin the subclause heading, by striking Update and inserting Updates ;\n**(ii)**\nby striking clause (i) to include and inserting \u201cclause (i)\u2014\n(aa) to include ;\n**(iii)**\nin item (aa) (as so designated), by striking the period at the end and inserting ; and ; and\n**(iv)**\nby adding at the end the following:\n(bb) not less frequently than once every 5 years after the date on which the management plan is submitted under that clause. .\n##### (c) Management and coordination\nSection 5001(b)(3) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( 43 U.S.C. 31k(b)(3) ) is amended\u2014\n**(1)**\nin subparagraph (D)\u2014\n**(A)**\nby redesignating clauses (ii) through (iv) as clauses (iii) through (v), respectively; and\n**(B)**\nby inserting after clause (i) the following:\n(ii) the Chief of the Forest Service; ; and\n**(2)**\nby adding at the end the following:\n(F) Implementation committee The Secretary shall establish an implementation committee that shall\u2014 (i) include representatives of\u2014 (I) each State agency or designee of a State agency subject to a cooperative agreement entered into under subparagraph (C); (II) institutions of higher education; and (III) each volcano observatory described in paragraph (1)(B)(i); and (ii) be responsible for providing to the Secretary recommended requirements, implementation steps, and performance standards for the System. (G) Communication The Secretary, in coordination with State emergency management partners, shall identify public communication and messaging responsibilities for each of the Secretary and the State emergency management partners to avoid confusion or duplication with respect to those responsibilities. .\n##### (d) Reauthorization\nSection 5001(c) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( 43 U.S.C. 31k(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking $55,000,000 and inserting $75,000,000 ; and\n**(B)**\nby striking 2023 and inserting 2033 ; and\n**(2)**\nin paragraph (2), by striking 2024 and inserting 2034 .",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
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
        "name": "Emergency Management",
        "updateDate": "2025-05-21T13:50:54Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1052is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "title": "A bill to amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to reauthorize the National Volcano Early Warning and Monitoring System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:25Z"
    },
    {
      "title": "A bill to amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to reauthorize the National Volcano Early Warning and Monitoring System, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T10:56:25Z"
    }
  ]
}
```
