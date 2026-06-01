# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3200?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3200
- Title: Critical Minerals and Manufacturing Support Act
- Congress: 119
- Bill type: HR
- Bill number: 3200
- Origin chamber: House
- Introduced date: 2025-05-05
- Update date: 2026-01-17T04:41:13Z
- Update date including text: 2026-01-17T04:41:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-05: Introduced in House

## Actions

- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3200",
    "number": "3200",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Critical Minerals and Manufacturing Support Act",
    "type": "HR",
    "updateDate": "2026-01-17T04:41:13Z",
    "updateDateIncludingText": "2026-01-17T04:41:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
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
      "actionDate": "2025-05-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T16:00:10Z",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "CO"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3200ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3200\nIN THE HOUSE OF REPRESENTATIVES\nMay 5, 2025 Mr. Ruiz (for himself and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the advanced manufacturing credit with respect to the production of battery components.\n#### 1. Short title\nThis Act may be cited as the Critical Minerals and Manufacturing Support Act .\n#### 2. Modification of advanced manufacturing production credit relating to battery production\n##### (a) Increase in credit amount for electrode active materials\nSection 45X(b)(1)(J) of the Internal Revenue Code of 1986 is amended by striking 10 percent and inserting 25 percent .\n##### (b) Special rules relating to production of electrode active materials\nSection 45X(b) of such Code is amended by adding at the end the following new paragraph:\n(5) Special rules relating to electrode active materials (A) Production costs The production of electrode active materials shall include the cost of raw materials, including material extraction from geological sources or waste products. .\n##### (c) Sourcing requirements with respect to qualifying battery components and applicable critical minerals\nSection 45X of such Code is amended by adding at the end the following new subsection:\n(e) Critical mineral and battery component sourcing requirements (1) Applicable critical minerals (A) In general No credit shall be allowed under this section with respect to a qualifying battery component unless the percentage of the value of the applicable critical minerals contained therein that were\u2014 (i) extracted or processed\u2014 (I) in the United States, or (II) in any country with which the United States has a free trade agreement in effect, or (ii) recycled, and reintegrated into the supply chain, in North America, is at least equal to the applicable percentage (as certified by the taxpayer in such form or manner as prescribed by the Secretary). (B) Applicable percentage For purposes of subparagraph (A), the applicable percentage shall be\u2014 (i) in the case of any qualifying battery component sold to an unrelated person during calendar year 2026, 70 percent, and (ii) in the case of any qualifying battery component sold to an unrelated person after December 31, 2026, 80 percent. (2) Qualifying battery components (A) In general No credit shall be allowed under this section with respect to a qualifying battery component unless the percentage of the value of the constituent elements, materials, and subcomponents contained therein that were produced, manufactured, or assembled in North America is at least equal to the applicable percentage (as certified by the taxpayer, in such form or manner as prescribed by the Secretary). (B) Applicable percentage For purposes of subparagraph (A), the applicable percentage shall be\u2014 (i) in the case of qualifying battery components sold to an unrelated person during calendar year 2026, 70 percent, (ii) in the case of qualifying battery components sold to an unrelated person during calendar year 2027, 80 percent, (iii) in the case of qualifying battery components sold to an unrelated person during calendar year 2028, 90 percent, and (iv) in the case of qualifying battery components sold to an unrelated person after December 31, 2028, 100 percent. (3) Regulations The Secretary shall, to the extent practicable, prescribe regulations similar to regulations prescribed under section 30D(e) to carry out the purposes of this subsection. .\n##### (d) Excluded entities\nSection 45X(c)(1) of such Code is amended by adding at the end the following new subparagraph:\n(C) Excluded entities The term eligible component shall not include any qualifying battery component with respect to which\u2014 (i) any of the applicable critical minerals contained therein were extracted, processed, or recycled by a foreign entity of concern (as defined in section 40207(a)(5) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18741(a)(5) )), and (ii) any of the constituent elements, materials, or subcomponents contained therein were produced, manufactured, or assembled by a foreign entity of concern (as so defined). The term foreign entity of concern shall include any entity that is directly or indirectly owned by a foreign entity of concern described in subparagraph (C) of section 40207(a)(5) of such Act. .\n##### (e) Modification of electrode active material definition\n**(1) In general**\nSection 45X(c)(5)(B)(i) of such Code is amended\u2014\n**(A)**\nby inserting electrode active precursor materials used in the production of cathode and anode materials, after anode materials, ,\n**(B)**\nby inserting binders, after anode foils, , and\n**(C)**\nby inserting solid state electrolytes, after including .\n**(2) Electrode active precursor materials**\nSection 45X(c)(5)(B)(i) of such Code is amended\u2014\n**(A)**\nby striking material .\u2014The term and inserting the following:\nmaterial.\u2014 (I) In general The term , and\n**(B)**\nby adding at the end the following new subclause:\n(II) Electrode active precursor material The term electrode active precursor material means any of the following materials which are of a sufficient grade to meet the purity specifications to supply the electrode active materials market: Cobalt sulfate, manganese sulfate, iron sulfate, lithium hydroxide, metallurgical silicon, phosphoric acid, iron phosphate, nickel manganese cobalt oxide, graphene, sulfur, synthetic or natural graphite pitch, or lithium carbonate. .\n##### (f) Certain silicon treated as applicable critical material\nSection 45X(c)(6) of such Code is amended by redesignating subparagraphs (T) through (Z) as subparagraphs (U) through (AA), respectively, and by inserting after subparagraph (S) the following new subparagraph:\n(T) Silicon Silicon which is silicon or silicon composite used as an electrode active material in battery anodes. .\n##### (g) Effective date\nThe amendments made by this section shall apply to components produced and sold after December 31, 2025.",
      "versionDate": "2025-05-05",
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
        "name": "Taxation",
        "updateDate": "2025-06-04T15:26:39Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3200ih.xml"
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
      "title": "Critical Minerals and Manufacturing Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Critical Minerals and Manufacturing Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to modify the advanced manufacturing credit with respect to the production of battery components.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:51Z"
    }
  ]
}
```
