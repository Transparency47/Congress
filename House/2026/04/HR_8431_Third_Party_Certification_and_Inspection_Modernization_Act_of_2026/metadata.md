# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8431?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8431
- Title: Third-Party Certification and Inspection Modernization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8431
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-04-28T15:05:07Z
- Update date including text: 2026-04-28T15:05:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8431",
    "number": "8431",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000619",
        "district": "6",
        "firstName": "Michael",
        "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
        "lastName": "Rulli",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Third-Party Certification and Inspection Modernization Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-28T15:05:07Z",
    "updateDateIncludingText": "2026-04-28T15:05:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
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
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:04:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8431ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8431\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. Rulli introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to expand a program under which third-parties are accredited to conduct food safety audits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Third-Party Certification and Inspection Modernization Act of 2026 .\n#### 2. Expansion of the accredited third-party certification program\n##### (a) Revised definitions\nSection 808 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 384d ) is amended\u2014\n**(1)**\nby amending subsection (a)(6) to read as follows:\n(6) Eligible entity The term eligible entity means a foreign or domestic entity, including a foreign or domestic facility subject to registration under section 415, in the food supply chain that chooses to be audited by an accredited third-party auditor or the audit agent of such accredited third-party auditor. ; and\n**(2)**\nby amending subsection (a)(7) to read as follows:\n(7) Regulatory audit The term \u2018regulatory audit\u2019 means an audit of an eligible entity\u2014 (A) to determine whether such entity is in compliance with the provisions of this Act; and (B) the results of which determine\u2014 (i) whether an article of food manufactured, processed, packed, or held by such entity is eligible to receive a food certification under section 801(q); (ii) whether a facility is eligible to receive a facility certification under section 806 for purposes of participating in the program under section 806; or (iii) whether a facility is eligible to receive a food or facility certification for other purposes described in subsection (c)(2)(B)(iii). .\n##### (b) Removing Limitations on the Use of Certifications\nSection 808(c)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 384d(c)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking food certification, described in section 801(q), or facility certification under section 806(a), as appropriate, to accompany each food shipment for import into the United States from an eligible entity, and inserting food certification or facility certification for purposes described in subparagraph (B), as appropriate, ; and\n**(2)**\nby amending subparagraph (B) to read as follows:\n(B) Purpose of certification (i) Certifications concerning imported foods The Secretary shall use certification provided by accredited third-party auditors to determine, in conjunction with any other assurances the Secretary may require under section 801(q), whether a food satisfies the requirements of such section. (ii) Voluntary qualified importer program The Secretary shall use certification provided by accredited third-party auditors to determine whether a facility is eligible to be a facility from which food may be offered for import under the voluntary qualified importer program under section 806. (iii) Analyzing risks and prioritizing inspections and other regulatory activities The Secretary may consider the results of regulatory audits and food or facility certifications provided by accredited third-party auditors under this section in analyzing risks and prioritizing inspections and other regulatory activities as appropriate for the protection of public health. .\n##### (c) Technical and conforming amendments\n**(1)**\nSection 808(b)(1)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 384d(b)(1)(A) ) is amended to read as follows:\n(A) Recognition of accreditation bodies Not later than 2 years after the date of enactment of the Third-Party Certification and Inspection Modernization Act of 2026, the Secretary shall establish a system for the recognition of accreditation bodies that accredit third-party auditors to certify that eligible entities meet the applicable requirements of this section. .\n**(2)**\nSection 808(c) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 384d(c) ) is amended\u2014\n**(A)**\nin paragraphs (1)(B) and (2)(A), by striking (or, in the case of direct accreditation under subsection (b)(1)(A)(ii), the Secretary) ;\n**(B)**\nin paragraph (2)(C)(i), by striking food certification under section 801(q) or a facility certification described under subparagraph (B) and inserting food certification or a facility certification described under this section ;\n**(C)**\nin paragraph (6)\u2014\n**(i)**\nin subparagraph(A)(i), by striking food certified under section 801(q) or from a facility certified under paragraph (2)(B) and inserting food or facility certified under this section ; and\n**(ii)**\nin subparagraph (C)(ii), by striking requirements under section 801(q) of certifying the food, or the requirements under paragraph (2)(B) of certifying the entity and inserting requirements for certifying the food or facility under this section ; and\n**(D)**\nin paragraph (7)(B)(i), by striking through direct accreditation under subsection (b)(1)(A)(ii) or .\n**(3)**\nSection 808(d) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 384d(d) ) is amended\u2014\n**(A)**\nin paragraph (1), by striking or at the end;\n**(B)**\nin paragraph (2), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding the following:; and\n(3) otherwise seeks certification for purposes of subsection (c)(2)(B)(iii). .\n##### (d) Identification and Inspection of Facilities\nSection 421(a)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350j(a)(1) ) is amended\u2014\n**(1)**\nby redesignating subparagraph (F) as subparagraph (G); and\n**(2)**\nby inserting after subparagraph (E) the following:\n(F) Whether the facility that manufactured, processed, packed, or held such food holds a certification demonstrating compliance with a third-party food safety standard that has been determined by the Secretary to be aligned with regulations issued by the Food and Drug Administration relating to preventive controls to ensure the safety of human food. .",
      "versionDate": "2026-04-22",
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
        "updateDate": "2026-04-28T15:05:06Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8431ih.xml"
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
      "title": "Third-Party Certification and Inspection Modernization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Third-Party Certification and Inspection Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to expand a program under which third-parties are accredited to conduct food safety audits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:26Z"
    }
  ]
}
```
