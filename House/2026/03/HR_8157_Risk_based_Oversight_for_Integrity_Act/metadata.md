# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8157
- Title: Risk-based Oversight for Integrity Act
- Congress: 119
- Bill type: HR
- Bill number: 8157
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-03-30T17:37:23Z
- Update date including text: 2026-03-30T17:37:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-03-27: Introduced in House

## Actions

- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8157",
    "number": "8157",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "W000829",
        "district": "8",
        "firstName": "Tony",
        "fullName": "Rep. Wied, Tony [R-WI-8]",
        "lastName": "Wied",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Risk-based Oversight for Integrity Act",
    "type": "HR",
    "updateDate": "2026-03-30T17:37:23Z",
    "updateDateIncludingText": "2026-03-30T17:37:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:33:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8157ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8157\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Mr. Wied (for himself and Mr. Riley of New York ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Organic Foods Production Act of 1990 to modernize oversight by directing a study on risk-based oversight, defining risk to organic integrity, and authorizing regulatory reforms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Risk-based Oversight for Integrity Act .\n#### 2. Definitions of risk to organic integrity and oversight protocols\nSection 2103 of the Organic Foods Production Act of 1990 ( 7 U.S.C. 6502 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (20) through (22) as paragraphs (22) through (24), respectively;\n**(2)**\nby redesignating paragraphs (16) through (19) as paragraphs (17) through (20), respectively;\n**(3)**\nby inserting after paragraph (15) the following:\n(16) Oversight protocols The term oversight protocols means the regulations, policies, and procedures issued by the Secretary under the authorities provided in sections 2104, 2107, 2114, 2115, 2116, and 2120. ; and\n**(4)**\nby inserting after paragraph (20), as so redesignated, the following:\n(21) Risk to organic integrity The term risk to organic integrity means the likelihood that a product marketed as organically produced is, or contains, an agricultural product that was not produced using a system of organic farming in compliance with this title, not processed in compliance with this title, or both. .\n#### 3. Modernization of inspection requirements\nParagraph (5) of section 2107(a) of the Organic Foods Production Act of 1990 ( 7 U.S.C. 6506(a) ) is amended to read as follows:\n(5) provide for annual inspections by the certifying agent of each farm and handling operation that has been certified under this title, which inspections shall be\u2014 (A) in the case of a farm or handling operation located outside of the United States, conducted on-site; (B) in the case of a farm or handling operation site located in the United States, conducted on-site once every three years with intervening annual inspections being conducted on-site or virtually based on the farm\u2019s or handling operation\u2019s risk to organic integrity, as determined by the Secretary; and (C) in the case of a handling operation that acquires but does not physically receive, process, package, or store organic product, conducted through inspection methods, including virtual methods, that provide sufficient assurance of compliance, as determined by the Secretary; .\n#### 4. Study and reform of National Organic Program oversight protocols\nThe Organic Foods Production Act of 1990 ( 7 U.S.C. 6501 et seq. ) is amended by inserting after section 2122A ( 7 U.S.C. 6521a ) the following:\n2122B. Study and reform of National Organic Program oversight protocols (a) Study Not later than 12 months after the date of enactment of this section, the Secretary shall conduct a comprehensive study for the purpose of determining whether the establishment of oversight protocols based on risk to organic integrity and the implementation of related reforms are necessary and appropriate. (b) Elements (1) In general In conducting the study under subsection (a), the Secretary shall examine the feasibility, opportunities, and implications of implementing oversight protocols that\u2014 (A) are based on risk to organic integrity; (B) include differential treatment of non-compliance that increases the risk to organic integrity versus non-compliance that does not; (C) adopt standardized organic plans under section 2114 aligned with the risk to organic integrity; (D) include a multi-tiered approach to certification aligned with the risk to organic integrity and the scale of the organic operation; and (E) provide increased guidance and interpretations of standards and criteria established under this title given by the National Organic Program to certifying agents and to certified organic farms and handling operations. (2) Consideration of relevant factors In administering paragraph (1), the Secretary shall, with respect to certified organic farms, certified organic handling operations, and certifying agents, take into account\u2014 (A) the scope of certification or accreditation of each entity; (B) the scale and complexity of each entity; (C) the domestic or international location of each entity; (D) the history of compliance of each entity; and (E) other relevant factors. (c) Report Not later than 18 months after the date of enactment of this section, the Secretary shall submit to the appropriate congressional committees, and make publically available on the websites of the Department of Agriculture, a report describing the findings of the study conducted under subsection (a). (d) Consultation In conducting the study under subsection (a), the Secretary shall consult with\u2014 (1) the National Organic Standards Board; (2) certifying agents; (3) certified organic farms and handling operations; (4) organic consumers; and (5) other relevant organic stakeholders. (e) Authority to establish additional terms and conditions (1) Issuance of regulations Based on the findings described in the report under subsection (c), and after consultation with the appropriate congressional committees, the Secretary may issue regulations to establish or modify oversight protocols under this title that the Secretary determines are necessary and appropriate, provided such regulations maintain strong organic integrity, support a resilient domestic organic sector, and are consistent with the requirements of this title. (2) Reducing oversight costs; prioritization In issuing the regulations under paragraph (1), the Secretary may seek to\u2014 (A) reduce oversight costs and administrative burdens for certified organic farms, certified organic handling operations, and certifying agents that present a lower risk to organic integrity; or (B) prioritize oversight resources for activities that present a higher risk to organic integrity. (f) Appropriate congressional committees defined In this section, the term appropriate congressional committees means\u2014 (1) the Committee on Agriculture of the House of Representatives; and (2) the Committee on Agriculture, Nutrition, and Forestry of the Senate. (g) Rule of construction Nothing in this section shall be construed to limit the Secretary\u2019s authority to enforce compliance with this title to protect organic integrity. .",
      "versionDate": "2026-03-27",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-30T17:37:23Z"
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
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8157ih.xml"
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
      "title": "Risk-based Oversight for Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Risk-based Oversight for Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-28T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Organic Foods Production Act of 1990 to modernize oversight by directing a study on risk-based oversight, defining risk to organic integrity, and authorizing regulatory reforms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T08:18:27Z"
    }
  ]
}
```
