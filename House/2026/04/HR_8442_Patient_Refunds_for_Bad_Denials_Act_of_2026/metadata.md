# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8442?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8442
- Title: Patient Refunds for Bad Denials Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8442
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-05-13T19:50:46Z
- Update date including text: 2026-05-13T19:50:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8442",
    "number": "8442",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001119",
        "district": "2",
        "firstName": "Angie",
        "fullName": "Rep. Craig, Angie [D-MN-2]",
        "lastName": "Craig",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Patient Refunds for Bad Denials Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T19:50:46Z",
    "updateDateIncludingText": "2026-05-13T19:50:46Z"
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
          "date": "2026-04-22T15:00:30Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8442ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8442\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Ms. Craig (for herself and Mr. Ryan ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXVII of the Public Health Service Act to establish civil liability for health insurance issuers with high levels of claims denials.\n#### 1. Short title\nThis Act may be cited as the Patient Refunds for Bad Denials Act of 2026 .\n#### 2. Establishing civil liability for health insurance issuers with high levels of claims denials\n##### (a) In general\nTitle XXVII of the Public Health Service Act ( 42 U.S.C. 300gg et seq. ) is amended by adding at the end the following new part:\nF Claims denials 2799C\u20131. Civil liability for high rates of claims denials (a) In general The Secretary may impose on each health insurance issuer offering group or individual health insurance coverage for a plan year beginning on or after January 1, 2027, a civil monetary penalty not to exceed the amount specified in subsection (e) if the Secretary finds that any such coverage offered by such issuer during such plan year had an claims denial percentage of 25 percent (or such lower percent as the Secretary may specify) or greater. (b) Claims denial percentage (1) In general For purposes of this section, the term claims denial percentage means, with respect to group or individual health insurance coverage and a plan year, the percentage of claims for items and services furnished during such plan year that the Secretary determines, pursuant to audits conducted under subsection (c), were denied. (2) Exclusion of certain claims A claim denied on the basis of fraud or lack of medical necessity that the Secretary determines, pursuant to audits conducted under subsection (c), were correctly denied shall not be treated as a denied claim for purposes of clause (i). (3) Evaluations of denied claims In assessing whether a claim that was denied by a health insurance issuer offering group or individual health insurance coverage on the basis of fraud was correctly denied for purposes of determining the claims denial percentage of such coverage, the Secretary shall find such claim to have been correctly denied only if such issuer provides sufficient information to the Secretary to demonstrate that such claim was fraudulent. (c) Audits The Secretary may conduct such audits of group and individual health insurance coverage as the Secretary determines appropriate for purposes of ascertaining the claims denial percentage of such coverage. (d) Distribution of amounts The Secretary shall distribute on a pro rata basis to individuals enrolled during a plan year in group or individual health insurance coverage offered by a health insurance issuer which is subject to a civil monetary penalty imposed under this section with respect to such plan year an amount equal to amounts collected under this section for such penalties so imposed. (e) Amount specified (1) In general For purposes of subsection (a), the amount specified in this subsection is, with respect to a health insurance issuer\u2014 (A) $10,000,000; plus (B) an additional $2,000,000 for every percentage point by which the claims denial percentage of such issuer exceeds 25 percent. (2) Inflation adjustments The Secretary may adjust the amounts specified in this subsection for 2028 and each subsequent year to account for the change in the consumer price index for all urban consumers over the preceding year. (3) Considerations in imposition In determining the amount of a civil monetary penalty under this section, the Secretary may take into account any efforts made by the health insurance issuer to reduce the claims denial percentage of health insurance coverage offered by such issuer. .\n##### (b) Consumer protections\n**(1) In general**\nSubpart II of part A of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u201311 et seq. ) is amended by adding at the end the following new section:\n2730. Transparency of information (a) In general A health insurance issuer offering group or individual health insurance coverage shall, in the case such issuer denies a claim for an item or service furnished to an individual on the basis that such item or service was not medically necessary, provide to such individual a notice containing\u2014 (1) the issuer\u2019s medical necessity standards for such item or service; and (2) an explanation of why such item or service so furnished failed to meet such standards. (b) Base claims denial rate A health insurance issuer offering group or individual health insurance coverage shall for each plan year submit to the Secretary the percentage of claims that were denied under such coverage for any reason. .\n**(2) Effective date**\nThe amendment made by this subsection shall apply with respect to plan years beginning on or after January 1, 2027.",
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
        "updateDate": "2026-05-13T19:50:46Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8442ih.xml"
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
      "title": "Patient Refunds for Bad Denials Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Patient Refunds for Bad Denials Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXVII of the Public Health Service Act to establish civil liability for health insurance issuers with high levels of claims denials.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:28Z"
    }
  ]
}
```
