# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4460?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4460
- Title: SAFE Guidance Act
- Congress: 119
- Bill type: HR
- Bill number: 4460
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported by the Yeas and Nays: 26 - 23.
- 2025-09-08 - Calendars: Placed on the Union Calendar, Calendar No. 208.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-251.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-251.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported by the Yeas and Nays: 26 - 23.
- 2025-09-08 - Calendars: Placed on the Union Calendar, Calendar No. 208.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-251.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-251.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4460",
    "number": "4460",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001204",
        "district": "9",
        "firstName": "Daniel",
        "fullName": "Rep. Meuser, Daniel [R-PA-9]",
        "lastName": "Meuser",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "SAFE Guidance Act",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-09-08",
      "calendarNumber": {
        "calendar": "U00208"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 208.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported by the Committee on Financial Services. H. Rept. 119-251.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Financial Services. H. Rept. 119-251.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 26 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
        "item": [
          {
            "date": "2025-09-08T17:47:29Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-23T17:00:14Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-22T17:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-16T14:05:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4460ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4460\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Meuser introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require a guidance clarity statement on certain financial agency guidance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Agency Fiat Enforcement of Guidance Act or the SAFE Guidance Act .\n#### 2. Guidance clarity statement required\n##### (a) In general\nThe head of each financial agency shall include a guidance clarity statement as described in subsection (b) on any guidance issued by that financial agency on and after the date of the enactment of this Act.\n##### (b) Guidance clarity statement\nA guidance clarity statement required under subsection (a) shall be displayed prominently on the first page of the document and shall include the following: This guidance does not have the force and effect of law and therefore does not establish any rights or obligations for any person and is not binding on the agency or the public. If this guidance suggests how regulated entities may comply with applicable statutes or regulations, noncompliance with this guidance does not conclusively establish a violation of applicable law. .\n##### (c) Definitions\nIn this section:\n**(1) Financial agency**\nThe term financial agency means the following:\n**(A)**\nThe Bureau of Consumer Financial Protection.\n**(B)**\nThe Department of Housing and Urban Development.\n**(C)**\nThe Department of the Treasury.\n**(D)**\nThe Federal Deposit Insurance Corporation.\n**(E)**\nThe Federal Housing Finance Agency.\n**(F)**\nThe Board of Governors of the Federal Reserve System.\n**(G)**\nThe National Credit Union Administration.\n**(H)**\nThe Office of the Comptroller of the Currency.\n**(I)**\nThe Securities and Exchange Commission.\n**(2) Guidance**\nThe term guidance means a financial agency statement of general applicability, intended to have a future effect on the behavior of regulated parties, that sets forth a policy on a statutory, regulatory, or technical issue, or an interpretation of a statute or regulation, but does not include\u2014\n**(A)**\na rule promulgated pursuant to notice and comment under section 553 of title 5, United States Code;\n**(B)**\na rule exempt from rulemaking requirements under section 553(a) of title 5, United States Code;\n**(C)**\na rule of financial agency organization, procedure, or practice;\n**(D)**\na decision of a financial agency adjudication under section 554 of title 5, United States Code, or any similar statutory provision;\n**(E)**\ninternal guidance directed to the issuing financial agency or other agency that is not intended to have a substantial future effect on the behavior of regulated parties; or\n**(F)**\ninternal executive branch legal advice or legal opinions addressed to executive branch officials.",
      "versionDate": "2025-07-16",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4460rh.xml",
      "text": "IB\nUnion Calendar No. 208\n119th CONGRESS\n1st Session\nH. R. 4460\n[Report No. 119\u2013251]\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Meuser introduced the following bill; which was referred to the Committee on Financial Services\nSeptember 8, 2025 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo require a guidance clarity statement on certain financial agency guidance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Agency Fiat Enforcement of Guidance Act or the SAFE Guidance Act .\n#### 2. Guidance clarity statement required\n##### (a) In general\nThe head of each financial agency shall include a guidance clarity statement as described in subsection (b) on any guidance issued by that financial agency on and after the date of the enactment of this Act.\n##### (b) Guidance clarity statement\nA guidance clarity statement required under subsection (a) shall be displayed prominently on the first page of the document and shall include the following: This guidance does not have the force and effect of law and therefore does not establish any rights or obligations for any person and is not binding on the agency or the public. If this guidance suggests how regulated entities may comply with applicable statutes or regulations, noncompliance with this guidance does not conclusively establish a violation of applicable law. .\n##### (c) Definitions\nIn this section:\n**(1) Financial agency**\nThe term financial agency means the following:\n**(A)**\nThe Bureau of Consumer Financial Protection.\n**(B)**\nThe Department of Housing and Urban Development.\n**(C)**\nThe Department of the Treasury.\n**(D)**\nThe Federal Deposit Insurance Corporation.\n**(E)**\nThe Federal Housing Finance Agency.\n**(F)**\nThe Board of Governors of the Federal Reserve System.\n**(G)**\nThe National Credit Union Administration.\n**(H)**\nThe Office of the Comptroller of the Currency.\n**(I)**\nThe Securities and Exchange Commission.\n**(2) Guidance**\nThe term guidance means a financial agency statement of general applicability, intended to have a future effect on the behavior of regulated parties, that sets forth a policy on a statutory, regulatory, or technical issue, or an interpretation of a statute or regulation, but does not include\u2014\n**(A)**\na rule promulgated pursuant to notice and comment under section 553 of title 5, United States Code;\n**(B)**\na rule exempt from rulemaking requirements under section 553(a) of title 5, United States Code;\n**(C)**\na rule of financial agency organization, procedure, or practice;\n**(D)**\na decision of a financial agency adjudication under section 554 of title 5, United States Code, or any similar statutory provision;\n**(E)**\ninternal guidance directed to the issuing financial agency or other agency that is not intended to have a substantial future effect on the behavior of regulated parties; or\n**(F)**\ninternal executive branch legal advice or legal opinions addressed to executive branch officials.",
      "versionDate": "2025-09-08",
      "versionType": "Reported in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-20",
        "text": "Placed on the Union Calendar, Calendar No. 535."
      },
      "number": "6955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Act",
      "type": "HR"
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
        "item": {
          "name": "Government information and archives",
          "updateDate": "2025-08-27T17:47:24Z"
        }
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-30T14:03:54Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4460ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4460rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "SAFE Guidance Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-09-09T07:23:26Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Stop Agency Fiat Enforcement of Guidance Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-09-09T07:23:26Z"
    },
    {
      "title": "SAFE Guidance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-19T07:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Guidance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-19T07:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Agency Fiat Enforcement of Guidance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-19T07:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a guidance clarity statement on certain financial agency guidance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-19T07:03:29Z"
    }
  ]
}
```
