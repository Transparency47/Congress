# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1248?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1248
- Title: EASE Act
- Congress: 119
- Bill type: S
- Bill number: 1248
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2025-12-05T22:49:24Z
- Update date including text: 2025-12-05T22:49:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1248",
    "number": "1248",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001190",
        "district": "",
        "firstName": "Markwayne",
        "fullName": "Sen. Mullin, Markwayne [R-OK]",
        "lastName": "Mullin",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "EASE Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:24Z",
    "updateDateIncludingText": "2025-12-05T22:49:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T16:25:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1248is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1248\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Mullin (for himself, Mr. Padilla , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XI of the Social Security Act to require the Center for Medicare and Medicaid Innovation to test a model to improve access to specialty health services for certain Medicare and Medicaid beneficiaries.\n#### 1. Short title\nThis Act may be cited as the Ensuring Access to Specialty Care Everywhere Act or the EASE Act .\n#### 2. Requiring the Center for Medicare and Medicaid Innovation to test a model to improve access to specialty health services for certain Medicare and Medicaid beneficiaries\n##### (a) In general\nSection 1115A of the Social Security Act ( 42 U.S.C. 1315a ) is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A), in the third sentence, by inserting , and shall include the model described in subparagraph (B)(xxviii) before the period at the end; and\n**(B)**\nin subparagraph (B), by adding at the end the following new clause:\n(xxviii) The Specialty Health Care Services Access Model described in subsection (h). ; and\n**(2)**\nby adding at the end the following new subsection:\n(h) Specialty Health Care Services Access Model (1) In general For purposes of subsection (b)(2)(B)(xxviii), the Specialty Health Care Services Access Model described in this subsection is a model under which the Secretary enters into an agreement with one or more provider networks selected in accordance with paragraph (2) for purposes of furnishing specialty health care services (as specified by the Secretary) to eligible individuals through the use of digital modalities (such as telehealth and other remote technologies) in coordination with such individuals\u2019 primary care providers. (2) Selection of provider networks The Secretary shall select one or more networks of providers for purposes of furnishing services under the model described in paragraph (1). Any such network so selected shall\u2014 (A) be comprised of at least 50 Federally qualified health centers, rural health clinics, critical access hospitals, or rural emergency hospitals, at least half of which are located in rural areas (as defined by the Administrator of the Health Resources and Services Administration); (B) be a nonprofit entity under section 501(c)(3) of the Internal Revenue Code of 1986; (C) have an established record of supporting the delivery of health care in rural and underserved communities in multiple regions throughout the country; and (D) have the ability to collect, exchange, and evaluate data for purposes of the model described in paragraph (1). (3) Eligible individual defined For purposes of this subsection, the term eligible individual means an individual\u2014 (A) who\u2014 (i) is entitled to benefits under part A of title XVIII or enrolled under part B of such title; or (ii) is enrolled under the Medicaid program under title XIX or the Children's Health Insurance Program under title XXI and meets all components for eligibility for medical assistance, child health assistance, or pregnancy-related assistance (as applicable), including those described in sections 1902(a)(46)(B) and 1137(d); and (B) who is located in a rural or underserved area (as specified by the Secretary). .\n##### (b) Limitation\nAny amounts appropriated or allocated to carry out the amendments made by this section shall be subject to the requirements contained in Public Law 117\u2013328 for funds for programs authorized under sections 330 through 340 of the Public Health Service Act (42 U.S.C. 254b through 256).",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-01",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2533",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "EASE Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-01T15:00:10Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1248is.xml"
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
      "title": "EASE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "EASE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Access to Specialty Care Everywhere Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XI of the Social Security Act to require the Center for Medicare and Medicaid Innovation to test a model to improve access to specialty health services for certain Medicare and Medicaid beneficiaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:18:29Z"
    }
  ]
}
```
