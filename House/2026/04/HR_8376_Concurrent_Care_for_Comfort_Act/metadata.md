# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8376?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8376
- Title: Concurrent Care for Comfort Act
- Congress: 119
- Bill type: HR
- Bill number: 8376
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-05-22T10:23:36Z
- Update date including text: 2026-05-22T10:23:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-20 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8376",
    "number": "8376",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "K000376",
        "district": "16",
        "firstName": "Mike",
        "fullName": "Rep. Kelly, Mike [R-PA-16]",
        "lastName": "Kelly",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Concurrent Care for Comfort Act",
    "type": "HR",
    "updateDate": "2026-05-22T10:23:36Z",
    "updateDateIncludingText": "2026-05-22T10:23:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-20T16:01:50Z",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8376ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8376\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. Kelly of Pennsylvania (for himself and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to clarify the policy for coverage under the Medicare program for palliative dialysis services, and clarify separate payment for such palliative dialysis services, furnished by renal dialysis facilities and providers of services to certain individuals electing hospice care, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Concurrent Care for Comfort Act .\n#### 2. Clarification and application of policy providing for coverage of concurrent palliative dialysis services and hospice care to individuals electing hospice care\n##### (a) In general\nSection 1812(d)(2)(A) of the Social Security Act ( 42 U.S.C. 1395d(d)(2)(A) ) is amended by inserting , to palliative dialysis services (as defined in section 1881(b)(15)(E)) furnished by a provider of services or renal dialysis facility to a palliative dialysis eligible individual (as defined in such section), after (if not an employee of the hospice program) .\n##### (b) Separate payment for palliative dialysis services furnished by providers of services and kidney dialysis facilities\n**(1) Payment separate from hospice care bundle**\nSection 1814(i) of the Social Security Act ( 42 U.S.C. 1395f(i) ) is amended by adding at the end the following new paragraph:\n(8) In the case of palliative dialysis services (as defined in section 1881(b)(15)(E)) furnished by a provider of services or renal dialysis facility to a palliative dialysis eligible individual (as defined in such section) during a period of an election under section 1812(d)(1) made by such individual, the provider of services or renal dialysis facility shall bill and be paid for such dialysis in accordance with section 1881(b)(15). .\n**(2) Payment methodology**\nSection 1881(b) of the Social Security Act ( 42 U.S.C. 1395r(b) ) is amended by adding at the end the following new paragraph:\n(15) Payment for palliative dialysis services furnished to individuals electing hospice care (A) In general For 2026 and each subsequent year, the Secretary shall, taking into account the assessment and considerations described in subparagraph (B) and pursuant to rulemaking, establish a methodology for determining, with respect to a palliative dialysis eligible individual whose election under section 1812(d)(1) to receive hospice care is for a period occurring during such year, the payment amounts under this title for palliative dialysis services furnished by a provider of services or renal dialysis facility during such period to such individual in a facility or to such individual at home. (B) Considerations In implementing the methodology under subparagraph (A), the Secretary shall\u2014 (i) consider calculating payment amounts for such services based on the amounts that would otherwise be calculated under the system established under paragraph (14) for comparable renal dialysis services described in such paragraph; and (ii) consider, after assessing the resources directly or indirectly related to furnishing palliative dialysis services necessary for providers of services and renal dialysis facilities to furnish palliative dialysis services to palliative dialysis eligible individuals in a facility or to such individuals at home, any adjustments that should be applied in calculating such payments amounts based on such assessment. (C) Limitations (i) In general Subject to clause (ii), payment may not be made under this title for more than ten sessions of palliative dialysis services furnished to a palliative dialysis eligible individual. In the case of home dialysis, including peritoneal dialysis, this subparagraph shall be applied by converting the number of days of such dialysis to hemodialysis equivalent sessions, in accordance with the methodology specified in section 50 of Chapter 11 of the Medicare Benefit Policy Manual, or any successor to such section. (ii) Secretarial authority to modify limitation (I) Assessment and determination For 2029 the Secretary shall (and for any subsequent year, the Secretary may) pursuant to rulemaking\u2014 (aa) assess the appropriateness of the limitation specified under clause (i) for such year, based on data on determinations regarding coverage of palliative dialysis services furnished to palliative dialysis eligible individuals pursuant to this paragraph and stakeholder feedback on such coverage; and (bb) based on such assessment, determine for such year whether to apply a limit on the number of sessions of palliative dialysis services (other than the number specified under clause (i)) and, if so, specify such other number that is to be applied for such year. (II) Application of modified number limit For any year for which the Secretary specifies a number pursuant to subclause (I)(bb) other than the number specified in clause (i), clause (i) shall be applied as if the reference to ten sessions were a reference to such different number of treatments specified by the Secretary. (D) Cost-sharing Under the methodology under subparagraph (A), the deductible and coinsurance provisions under this title that would apply with respect to kidney dialysis services for which payment may be made under this section (other than this paragraph) shall also apply with respect to palliative dialysis services furnished to a palliative dialysis eligible individual for which payment is made pursuant to this paragraph. (E) Palliative dialysis services and palliative dialysis eligible individual defined For purposes of this paragraph: (i) Palliative dialysis services The term palliative dialysis services means, with respect to a palliative dialysis eligible individual, dialysis services specified by the Secretary that are furnished to the individual (in a facility or at home) as palliative care, and not for purposes of treatment or maintenance, in accordance with a plan of care certified by the individual\u2019s physician in consultation with the interdisciplinary group described in section 1861(dd)(2)(B), and which may include other services specified by the Secretary, such as non-emergency transportation for which payment would otherwise be available under this section in connection with receipt of maintenance dialysis services. (ii) Palliative dialysis eligible individual The term palliative dialysis eligible individual means an individual with end-stage renal disease who makes an election under section 1812(d)(1) and who as of the date of such election was receiving renal dialysis services (as described in section 1881(b)(14)(B)). (F) Clarification None of the provisions of this paragraph shall affect coverage or payment under this title which would otherwise apply for renal dialysis services for treatment or maintenance for individuals with end-stage renal disease who make an election for hospice care under section 1812(d)(1) on the basis of a primary health condition other than a terminal condition that is not related to end-stage renal disease. .",
      "versionDate": "2026-04-20",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8376ih.xml"
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
      "title": "Concurrent Care for Comfort Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Concurrent Care for Comfort Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to clarify the policy for coverage under the Medicare program for palliative dialysis services, and clarify separate payment for such palliative dialysis services, furnished by renal dialysis facilities and providers of services to certain individuals electing hospice care, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:28Z"
    }
  ]
}
```
