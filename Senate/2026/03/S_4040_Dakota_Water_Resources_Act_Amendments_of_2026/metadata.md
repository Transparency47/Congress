# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4040?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4040
- Title: Dakota Water Resources Act Amendments of 2026
- Congress: 119
- Bill type: S
- Bill number: 4040
- Origin chamber: Senate
- Introduced date: 2026-03-10
- Update date: 2026-03-31T21:01:37Z
- Update date including text: 2026-03-31T21:01:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-10: Introduced in Senate
- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2026-03-10: Introduced in Senate

## Actions

- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-10",
    "latestAction": {
      "actionDate": "2026-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4040",
    "number": "4040",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Dakota Water Resources Act Amendments of 2026",
    "type": "S",
    "updateDate": "2026-03-31T21:01:37Z",
    "updateDateIncludingText": "2026-03-31T21:01:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-10",
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
      "actionDate": "2026-03-10",
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
          "date": "2026-03-10T20:22:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:36Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4040is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4040\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2026 Mr. Hoeven (for himself, Mr. Padilla , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend Public Law 89\u2013108 to modify the authorization of appropriations for State and Tribal, municipal, rural, and industrial water supplies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dakota Water Resources Act Amendments of 2026 .\n#### 2. Authorization of appropriations for State and Tribal, municipal, rural, and industrial water service\nSection 10 of Public Law 89\u2013108 (79 Stat. 433; 100 Stat. 424; 106 Stat. 4669; 114 Stat. 2763A\u2013291; 140 Stat. 74) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby redesignating subparagraph (D) as subparagraph (E); and\n**(ii)**\nby inserting after subparagraph (C) the following:\n(D) Additional amounts for certain projects (i) In general Subject to clauses (ii) through (iv), in addition to the amounts made available under subparagraphs (A), (B), and (C), there are authorized to be appropriated to carry out section 7(a)\u2014 (I) $120,000,000, as indexed, to complete all phases of the Northwest Area Water Supply Biota Water Treatment Plant and Pump Station Project, as described in the record of decision dated August 21, 2015; (II) $404,000,000, as indexed, to complete the McClusky Canal and Missouri River North Alternative for the Eastern North Dakota Alternate Water Supply Project, as described in the record of decision issued by the Bureau of Reclamation on January 15, 2021; (III) $50,000,000, as indexed, for the Southwest Pipeline Project to complete\u2014 (aa) the supplementary raw water intake and pump station described in the environmental assessment prepared by the Bureau of Reclamation entitled Finding of No Significant Impact of Environmental Assessment for Southwest Pipeline Project, Oliver, Mercer, North Dunn Service Area in Southwest North Dakota and dated April 2009; (bb) the main transmission line upgrades described in the final supplemental environmental assessment prepared by the Bureau of Reclamation entitled the Final Supplemental Environmental Assessment for Partial Funding of Design and Construction of an Expansion Water Treatment Plant in the City of Dickinson, North Dakota and Associated Water Transmission Facilities in Southwest North Dakota and dated February 2015; (cc) strategic hydraulic improvements; and (dd) rural distribution expansion; and (IV) $63,000,000, as indexed, for North Dakota rural water districts for water treatment and rural distribution expansion, to include the South Central Regional Water District North Burleigh Water Treatment Plant Expansion and Phase One of the Northeast North Dakota Long-Term Water Supply Project. (ii) Transfers Any amounts made available under any of subclauses (I) through (IV) of clause (i) may be transferred among the projects described in those subclauses, subject to the limitation that the initial amount authorized for any 1 project described in any of those subclauses may not be increased by more than 50 percent as a result of any transfers authorized under this clause. (iii) Final engineering reports Of the amounts made available under subclauses (III) and (IV) of clause (i), the Secretary may use such amounts as are necessary to complete the final engineering reports, to be completed not later than 2 years after the date of enactment of the Dakota Water Resources Act Amendments of 2026 , that determine the scope of, and identify the features necessary to complete, the projects described in those subclauses, as determined by the Secretary. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(ii)**\nby inserting after subparagraph (B) the following:\n(C) Other amounts (i) In general In addition to the amounts made available under subparagraphs (A)(ii) and (B), there is authorized to be appropriated to carry out section 7(d) $743,000,000, as indexed. (ii) Allocation The amount under clause (i) shall be allocated as follows: (I) Not more than $118,000,000, as indexed, shall be made available to the Secretary to complete the Spirit Lake Rural Water System within the Fort Totten Indian Reservation. (II) Not more than $275,000,000, as indexed, shall be made available to the Secretary to complete the Three Affiliated Tribes Rural Water System within the Fort Berthold Indian Reservation. (III) Not more than $240,000,000, as indexed, shall be made available to the Secretary to complete the Standing Rock Rural Water System within the Standing Rock Indian Reservation. (IV) Not more than $98,000,000, as indexed, shall be made available to the Secretary to complete the Turtle Mountain Rural Water System within the Turtle Mountain Indian Reservation. (V) $12,000,000, as indexed, shall be made available to the Secretary\u2014 (aa) to complete a feasibility study for the construction of a municipal, rural, and industrial water system to meet the drinking water needs of the Lake Traverse Rural Water System within the Lake Traverse Indian Reservation; and (bb) after completion of the feasibility study and a determination by the Secretary that the proposed project under item (aa) is technically and financially feasible in accordance with the reclamation laws, to begin construction of the municipal, rural, and industrial water system identified as the preferred alternative in the feasibility study. (iii) Final engineering reports Of the amounts made available under clause (i), the Secretary may use such amounts as are necessary to complete final engineering reports, to be completed not later than 2 years after the date of enactment of the Dakota Water Resources Act Amendments of 2026 , that determine the scope of, and identify the features necessary to complete, each of the rural water systems described in subclauses (I) through (IV) of clause (ii), as determined by the Secretary. ;\n**(2)**\nin subsection (c)(2), by striking subparagraph (B) and inserting the following:\n(B) $75,000,000 to carry out section 11, to remain available until expended. ; and\n**(3)**\nby striking subsection (e) and inserting the following:\n(e) Indexing (1) In general The $200,000,000 amount under subsection (a)(1)(B), the $200,000,000 amount under subsection (b)(1)(B), and the funds authorized under subparagraphs (A) and (B) of subsection (b)(2) shall be indexed as necessary to allow for ordinary fluctuations of construction costs incurred after the date of enactment of the Dakota Water Resources Act of 2000, as indicated by engineering cost indices applicable for the type of construction involved. (2) Additional amounts The $50,000,000 amount under subsection (a)(1)(C) shall be indexed as necessary to allow for ordinary fluctuations of construction costs incurred after the date of enactment of the Energy and Water Development and Related Agencies Appropriations Act, 2026, as indicated by engineering cost indices applicable for the type of construction involved. (3) Other amounts The funds authorized under subsections (b)(1)(D) and (b)(2)(C) shall be indexed as necessary to allow for ordinary fluctuations of construction costs incurred after the date of enactment of the Dakota Water Resources Act Amendments of 2026 , as indicated by engineering cost indices applicable for the type of construction involved. (4) Other cost ceilings All other authorized cost ceilings under this Act shall remain unchanged. .\n#### 3. Natural Resources Trust\nSection 11(a)(2)(B) of Public Law 89\u2013108 (79 Stat. 433; 100 Stat. 424; 114 Stat. 2763A\u2013292) is amended by striking and (b)(1)(B) and inserting , (b)(1)(B), and (b)(1)(D) .",
      "versionDate": "2026-03-10",
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
        "actionDate": "2026-03-19",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "8006",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Dakota Water Resources Act Amendments of 2026",
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
        "name": "Water Resources Development",
        "updateDate": "2026-03-31T21:01:37Z"
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
      "date": "2026-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4040is.xml"
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
      "title": "A bill to amend Public Law 89-108 to modify the authorization of appropriations for State and Tribal, municipal, rural, and industrial water supplies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:28Z"
    },
    {
      "title": "Dakota Water Resources Act Amendments of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dakota Water Resources Act Amendments of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:18Z"
    }
  ]
}
```
