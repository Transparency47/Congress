# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4477?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4477
- Title: PRICE Act
- Congress: 119
- Bill type: HR
- Bill number: 4477
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-04-15T16:31:22Z
- Update date including text: 2026-04-15T16:31:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4477",
    "number": "4477",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "PRICE Act",
    "type": "HR",
    "updateDate": "2026-04-15T16:31:22Z",
    "updateDateIncludingText": "2026-04-15T16:31:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "NE"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "OR"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "MI"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4477ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4477\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Bonamici (for herself, Mr. Bacon , and Ms. Salinas ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo establish a manufactured housing community improvement grant program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preservation and Reinvestment Initiative for Community Enhancement Act or the PRICE Act .\n#### 2. Manufactured housing community improvement grant program\nTitle I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 105(a) ( 42 U.S.C. 5305(a) ), in the matter preceding paragraph (1), by striking Activities and inserting Unless otherwise authorized under section 123, activities ; and\n**(2)**\nby adding at the end the following:\n123. Preservation and reinvestment for community enhancement (a) Definitions In this section: (1) Community development financial institution The term community development financial institution means an institution that has been certified as a community development financial institution (as defined in section 103 of the Riegle Community Development and Regulatory Improvement Act of 1994 ( 12 U.S.C. 4702 )) by the Secretary of the Treasury. (2) Eligible manufactured housing community The term eligible manufactured housing community means a manufactured housing community that\u2014 (A) is affordable to low- and moderate-income persons, as determined by the Secretary, but not more than 120 percent of the area median income; and (B) (i) is owned by the residents of the manufactured housing community through a resident-controlled entity such as a resident-owned cooperative; or (ii) will be maintained as such a community, and remain affordable for low- and moderate-income persons, to the maximum extent practicable and for the longest period feasible. (3) Eligible recipient The term eligible recipient means\u2014 (A) an eligible manufactured housing community; (B) a unit of general local government; (C) a housing authority; (D) a resident-owned community; (E) a resident-owned cooperative; (F) a nonprofit entity with housing expertise or a consortia of such entities; (G) a community development financial institution; (H) an Indian Tribe; (I) a tribally designated housing entity; (J) a State; or (K) any other entity that is\u2014 (i) an owner-operator of an eligible manufactured housing community; and (ii) working with an eligible manufactured housing community. (4) Indian Tribe The term Indian Tribe has the meaning given the term Indian tribe in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ). (5) Manufactured housing community The term manufactured housing community means\u2014 (A) any community, court, park, or other land under unified ownership developed and accommodating or equipped to accommodate the placement of manufactured homes, where\u2014 (i) spaces within such community are or will be primarily used for residential occupancy; (ii) all homes within the community are used for permanent occupancy; (iii) a majority of such occupied spaces within the community are occupied by manufactured homes, which may include homes constructed prior to enactment of the Manufactured Home Construction and Safety Standards; or (B) any community that meets the definition of manufactured housing community used for programs similar to the program under this section. (6) Resident health, safety, and accessibility activities The term resident health, safety, and accessibility activities means the reconstruction, repair, or replacement of manufactured housing and manufactured housing communities to\u2014 (A) protect the health and safety of residents; (B) address weatherization and reduce utility costs; or (C) address accessibility needs for residents with disabilities. (7) Tribally designated housing entity The term tribally designated housing entity has the meaning given the term in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ). (b) Establishment The Secretary shall, by notice, carry out a competitive grant program to award funds to eligible recipients to carry out eligible projects for development of or improvements in eligible manufactured housing communities. (c) Eligible projects (1) In general Amounts from grants under this section may be used for\u2014 (A) community infrastructure, facilities, utilities, and other land improvements in or serving an eligible manufactured housing community; (B) reconstruction or repair existing housing within an eligible manufactured housing community; (C) replacement of homes within an eligible manufactured housing community; (D) planning; (E) resident health, safety, and accessibility activities in homes in an eligible manufactured housing community; (F) land and site acquisition and infrastructure for expansion or construction of an eligible manufactured housing community; (G) resident and community services, including relocation assistance, eviction prevention, and down payment assistance; and (H) any other activity that\u2014 (i) is approved by the Secretary consistent with the requirements under this section; (ii) improves the overall living conditions of an eligible manufactured housing community, which may include the addition or enhancement of shared spaces such as community centers, recreational areas, or other facilities that support resident well-being and community engagement; and (iii) is necessary to protect the health and safety of the residents of the eligible manufactured housing community and the long-term affordability and sustainability of the community. (2) Replacement For purposes of subparagraphs (B) and (C) of paragraph (1), grants under this section\u2014 (A) may not be used for rehabilitation or modernization of units that were built before June 15, 1976; and (B) may only be used for disposition and replacement of units described in subparagraph (A), provided that any replacement housing complies with the Manufactured Home Construction and Safety Standards or is another allowed home, as determined by the Secretary. (d) Priority In awarding grants under this section, the Secretary shall prioritize applicants that will carry out activities that primarily benefit low- and moderate-income residents and preserve long-term housing affordability for residents of eligible manufactured housing communities. (e) Waivers The Secretary may waive or specify alternative requirements for any provision of law or regulation that the Secretary administers in connection with use of amounts made available under this section other than requirements related to fair housing, nondiscrimination, labor standards, and the environment, upon a finding that the waiver or alternative requirement is not inconsistent with the overall purposes of this section and that the waiver or alternative requirement is necessary to facilitate the use of amounts made available under this section. (f) Implementation (1) In general Any grant made under this section shall be made pursuant to criteria for selection of recipients of such grants that the Secretary shall by regulation establish and publish together with any notification of availability of amounts under this section. (2) Set aside of grant amounts The Secretary may set aside amounts provided under this section for grants to Indian Tribes and tribally designated housing entities. (g) Authorization of appropriations There is authorized to be appropriated to the Secretary such sums as may be necessary to carry out this section, which shall be in addition to any other funds appropriated to pursuant to this title. .",
      "versionDate": "2025-07-17",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "943",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PRICE Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-01",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 143."
      },
      "number": "2651",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ROAD to Housing Act of 2025",
      "type": "S"
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-11T16:34:41Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4477ih.xml"
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
      "title": "PRICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T06:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PRICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preservation and Reinvestment Initiative for Community Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a manufactured housing community improvement grant program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:31Z"
    }
  ]
}
```
