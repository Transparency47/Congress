# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/767?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/767
- Title: FLASH Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 767
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-03-01T14:35:45Z
- Update date including text: 2025-03-01T14:35:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/767",
    "number": "767",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000598",
        "district": "42",
        "firstName": "Robert",
        "fullName": "Rep. Garcia, Robert [D-CA-42]",
        "lastName": "Garcia",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "FLASH Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-01T14:35:45Z",
    "updateDateIncludingText": "2025-03-01T14:35:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:04:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr767ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 767\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Garcia of California introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize the Biomedical Advanced Research and Development Authority to award follow-on production contracts or transactions, procure supplies for experimental or test purposes, and acquire innovative commercial products and commercial services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fast-Track Logistics for Acquiring Supplies in a Hurry Act of 2025 or the FLASH Act of 2025 .\n#### 2. Authority to award follow-on production contracts or transactions, procure supplies for experimental or test purposes, and acquire innovative commercial products and commercial services\nSection 319L of the Public Health Service Act ( 42 U.S.C. 247d\u20137e ) is amended\u2014\n**(1)**\nin subsection (a)(6)(B), by amending clause (ii) to read as follows:\n(ii) design and development of\u2014 (I) tests and prototypes, including obtaining sufficient quantities for evaluation of such tests and prototypes; and (II) models, including animal models, for such testing and prototypes; ; and\n**(2)**\nin subsection (c)(5)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby redesignating clause (iv) as clause (v); and\n**(ii)**\nby inserting after clause (iii) the following new clause:\n(iv) Follow-on production contracts or transactions (I) In general A transaction entered into under this subparagraph for the design or development of a prototype may provide for the award of a follow-on production contract or transaction to the participants in the transaction. (II) Prototype subprojects A transaction entered into under this subparagraph includes all prototype subprojects awarded under the transaction to carry out authorities under this section. (III) Exception to competitive procedures Notwithstanding clause (ii), a follow-on production contract or transaction provided for in a transaction under this clause may be awarded to the participants in the transaction without the use of competitive procedures, even if explicit notification was not listed within the request for proposal for the transaction, if competitive procedures were used for the selection of parties for participation in the initial transaction. ; and\n**(B)**\nby adding at the end the following new subparagraphs:\n(I) Procurement for experimental or test purposes (i) In general The Secretary may purchase medical countermeasures, products, and supplies, chemical materials and reagents, manufacturing supplies, protective equipment, and such other supplies, including parts and accessories, and designs thereof, as the Secretary determines necessary for experimental or test purposes in the development of supplies that are necessary for national public health and health security. (ii) Procedures Notwithstanding subparagraph (A)(ii), the Secretary may make purchases under this subparagraph by contract, or by entering into a transaction other than a contract, using noncompetitive procedures. (J) Acquisition of innovative commercial products and commercial services using general solicitation competitive procedures (i) In general Notwithstanding subparagraph (A)(ii), the Secretary may acquire innovative commercial products and commercial services through a competitive selection of proposals resulting from a general solicitation and the peer review of such proposals. (ii) Treatment as competitive procedures Use of general solicitation competitive procedures under clause (i) shall be considered to be use of competitive procedures for purposes of chapter 33 of title 41, United States Code. (iii) Limitations (I) Transactions in excess of $100,000,000 The Secretary may not enter into a contract or agreement in excess of $100,000,000 using the authority under clause (i), unless the Secretary makes a written determination of the efficacy of the effort to meet mission needs of the Department of Health and Human Services. (II) Fixed-price Contracts or agreements entered into using the authority under clause (i) shall be fixed-price, including fixed-price incentive contracts. (iv) Congressional notification required (I) Submission Not later than 45 days after the award of a contract for an amount exceeding $100,000,000 using the authority under clause (i), the Secretary shall provide notification of such award to the Committee on Energy and Commerce and the Committee on Appropriations of the House of Representatives, and the Committee on Health, Education, Labor, and Pensions and the Committee on Appropriations of the Senate. (II) Contents Notification of an award under subclause (I) shall include the following: (aa) Description of the innovative commercial product or commercial service acquired. (bb) Description of the requirement, capability gap, or potential technological advancement with respect to which the innovative commercial product or commercial service acquired provides a solution or a potential new capability. (cc) Amount of the contract awarded. (dd) Identification of the contractor awarded the contract. (v) Innovative defined In this subparagraph, the term innovative , with respect to a commercial product or commercial service, means\u2014 (I) any technology, process, or method, including research and development, that is new as of the date of submission of a proposal; or (II) with respect to a technology, process, or method, including research and development, existing as of the date of submission of a proposal, any application of such technology, process, or method that is new to the Federal Government as of such date. .",
      "versionDate": "2025-01-28",
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
        "name": "Health",
        "updateDate": "2025-03-01T14:35:45Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr767ih.xml"
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
      "title": "FLASH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FLASH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fast-Track Logistics for Acquiring Supplies in a Hurry Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize the Biomedical Advanced Research and Development Authority to award follow-on production contracts or transactions, procure supplies for experimental or test purposes, and acquire innovative commercial products and commercial services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:24Z"
    }
  ]
}
```
