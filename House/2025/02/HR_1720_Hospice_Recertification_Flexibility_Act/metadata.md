# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1720?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1720
- Title: Hospice Recertification Flexibility Act
- Congress: 119
- Bill type: HR
- Bill number: 1720
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-09-02T19:13:07Z
- Update date including text: 2025-09-02T19:13:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1720",
    "number": "1720",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Hospice Recertification Flexibility Act",
    "type": "HR",
    "updateDate": "2025-09-02T19:13:07Z",
    "updateDateIncludingText": "2025-09-02T19:13:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "ME"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1720ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1720\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mrs. Miller of West Virginia (for herself, Mr. Golden of Maine , Ms. Van Duyne , Mr. Davis of North Carolina , Mr. Bean of Florida , and Mr. Morelle ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to extend certain telehealth flexibilities with respect to hospice care under the Medicare program, and to establish a modifier for recertifications of hospice care eligibility conducted through telehealth.\n#### 1. Short title\nThis Act may be cited as the Hospice Recertification Flexibility Act .\n#### 2. Extension of certain telehealth flexibilities\nSection 1814(a)(7)(D)(i)(II) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(D)(i)(II) ) is amended\u2014\n**(1)**\nby striking ending on March 31, 2025 and inserting ending on December 31, 2027 ; and\n**(2)**\nby inserting , except that this subclause shall not apply in the case of such an encounter with an individual occurring on or after January 1, 2026, if such individual is located in an area that has been subject to a moratorium on the enrollment of hospice programs under this title pursuant to section 1866(j)(7) for a period of not less than 6 months, if such individual is receiving hospice care from a provider that is subject to enhanced oversight under this title pursuant to section 1866(j)(3), or if such encounter is performed by a hospice physician or nurse practitioner who is not enrolled under section 1866(j) and is not an opt-out physician or practitioner (as defined in section 1802(b)(6)(D)) before the semicolon.\n#### 3. Establishment of modifier for recertifications of hospice care eligibility conducted through telehealth\nSection 1814(a)(7)(D)(i)(II) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(D)(i)(II) ), as amended by section 2, is further amended by inserting , but only if, in the case of such an encounter occurring on or after January 1, 2026, any hospice claim includes 1 or more modifiers or codes (as specified by the Secretary) to indicate that such encounter was conducted via telehealth after as determined appropriate by the Secretary .",
      "versionDate": "2025-02-27",
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
            "name": "Health care coverage and access",
            "updateDate": "2025-09-02T19:13:07Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-09-02T19:13:00Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2025-09-02T19:12:54Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-09-02T19:12:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-21T13:32:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1720",
          "measure-number": "1720",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1720v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Hospice Recertification Flexibility Act</strong></p><p>This bill extends until December 31, 2027, the ability of physicians and nurse practitioners to fulfill certain requirements for hospice care recertification under Medicare via telehealth.</p><p>Specifically, physicians and nurse practitioners may continue to fulfill the requirement of a face-to-face encounter with the hospice patient via telehealth. Such telehealth encounters must be identified with a specialized claims modifier for purposes of billing.</p><p>The bill's authorization does not apply (1) in areas in which there has been a moratorium for at least six months on the enrollment of new hospice programs under Medicare, Medicaid, or the Children's Health Insurance Program (CHIP) due to fraud, waste, or abuse; (2) to providers who are subject to enhanced oversight under Medicare, Medicaid, or CHIP; and (3) to practitioners who are not enrolled as Medicare providers and who have private contracts with Medicare patients that do not meet applicable opt-out requirements.</p>"
        },
        "title": "Hospice Recertification Flexibility Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1720.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Hospice Recertification Flexibility Act</strong></p><p>This bill extends until December 31, 2027, the ability of physicians and nurse practitioners to fulfill certain requirements for hospice care recertification under Medicare via telehealth.</p><p>Specifically, physicians and nurse practitioners may continue to fulfill the requirement of a face-to-face encounter with the hospice patient via telehealth. Such telehealth encounters must be identified with a specialized claims modifier for purposes of billing.</p><p>The bill's authorization does not apply (1) in areas in which there has been a moratorium for at least six months on the enrollment of new hospice programs under Medicare, Medicaid, or the Children's Health Insurance Program (CHIP) due to fraud, waste, or abuse; (2) to providers who are subject to enhanced oversight under Medicare, Medicaid, or CHIP; and (3) to practitioners who are not enrolled as Medicare providers and who have private contracts with Medicare patients that do not meet applicable opt-out requirements.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hr1720"
    },
    "title": "Hospice Recertification Flexibility Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Hospice Recertification Flexibility Act</strong></p><p>This bill extends until December 31, 2027, the ability of physicians and nurse practitioners to fulfill certain requirements for hospice care recertification under Medicare via telehealth.</p><p>Specifically, physicians and nurse practitioners may continue to fulfill the requirement of a face-to-face encounter with the hospice patient via telehealth. Such telehealth encounters must be identified with a specialized claims modifier for purposes of billing.</p><p>The bill's authorization does not apply (1) in areas in which there has been a moratorium for at least six months on the enrollment of new hospice programs under Medicare, Medicaid, or the Children's Health Insurance Program (CHIP) due to fraud, waste, or abuse; (2) to providers who are subject to enhanced oversight under Medicare, Medicaid, or CHIP; and (3) to practitioners who are not enrolled as Medicare providers and who have private contracts with Medicare patients that do not meet applicable opt-out requirements.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hr1720"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1720ih.xml"
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
      "title": "Hospice Recertification Flexibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T15:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hospice Recertification Flexibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T15:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to extend certain telehealth flexibilities with respect to hospice care under the Medicare program, and to establish a modifier for recertifications of hospice care eligibility conducted through telehealth.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T15:18:24Z"
    }
  ]
}
```
