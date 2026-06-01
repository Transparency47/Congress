# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6693?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6693
- Title: SALAMANDER Act
- Congress: 119
- Bill type: HR
- Bill number: 6693
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-02-03T09:05:42Z
- Update date including text: 2026-02-03T09:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6693",
    "number": "6693",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "SALAMANDER Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:42Z",
    "updateDateIncludingText": "2026-02-03T09:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:40:14Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6693ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6693\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Mr. Moore of North Carolina (for himself and Mr. Edwards ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act to establish expedited permitting procedures for post-natural disaster recovery activities, incorporating interagency coordination and best management practices to ensure timely rebuilding while protecting endangered species, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Authorizations for Listed At-risk Marine and Aquatic Natural Disaster Emergency Resources Act or the SALAMANDER Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nNatural disasters cause significant damage to communities and infrastructure, requiring rapid and efficient recovery efforts.\n**(2)**\nTimely repair and restoration of damaged property and assets after a natural disaster are essential for public safety, economic stability, and the swift return of private property to rightful owners.\n**(3)**\nThe Corps of Engineers nationwide permit program serves as an efficient mechanism for managing activities that involve discharges into and rehabilitation of waters of the United States, as defined in the Federal Water Pollution Control Act.\n**(4)**\nThe Endangered Species Act of 1973 requires Federal agencies to consult with the Directors of the United States Fish and Wildlife Service and the National Marine Fisheries Service, as applicable, to avoid actions that could jeopardize listed species or critical habitats of such species.\n**(5)**\nWhile environmental protection is critical, current consultation processes can sometimes contribute to delays in post-disaster recovery.\n**(6)**\nA comprehensive, coordinated, and expedited approach for post-disaster permitting that leverages the biological expertise of the United States Fish and Wildlife Service and the National Marine Fisheries Service, and incorporates approved best management practices, will reduce regulatory delays while maintaining robust environmental safeguards.\n#### 3. General permits for dredged or fill material disposal in post-disaster recovery\nSection 404(e) of the Federal Water Pollution Control Act ( 33 U.S.C. 1344(e) ) is amended by adding at the end the following:\n(3) General permits for post-disaster recovery activities (A) In general For any geographic area with respect to which the President has declared under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) that a major disaster or emergency exists, the Secretary may issue or modify a general permit under this subsection for any category of activities\u2014 (i) the Secretary develops pursuant to a programmatic consultation with the Secretary of the Interior, Secretary of Commerce, and Secretary of Agriculture, as applicable, under section 7(a)(2) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(a)(2) ); and (ii) which activities\u2014 (I) are directly related to recovering from the major disaster or emergency; and (II) the Secretary of the Interior, Secretary of Commerce, and Secretary of Agriculture, as applicable, have determined through such programmatic consultation will avoid or minimize adverse effects on any species listed as a threatened species or an endangered species under section 4 of the Endangered Species Act of 1973 ( 16 U.S.C. 1533 ) and the critical habitat (as such term is defined in section 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 )) of such a species when adhering to best management practices described in subparagraph (B). (B) Best management practices A general permit issued or modified under this paragraph shall require the use of best management practices that have been\u2014 (i) agreed upon by the Secretary and, as applicable, the Secretary of the Interior, Secretary of Commerce, and Secretary of Agriculture; and (ii) designed to avoid or minimize adverse effects on species listed as threatened species or endangered species under section 4 of the Endangered Species Act of 1973 ( 16 U.S.C. 1533 ) and the critical habitat (as such term is defined in section 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 )) of such species. (C) Period A general permit, or modification to a general permit, issued under this paragraph shall be for the period of 18 months beginning on the date of the declaration of the major disaster or emergency by the President. (D) Effect on individual consultation An activity authorized by a general permit issued or modified under this paragraph and carried out in accordance with the requirements of such general permit is not subject to section 7(a)(2) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(a)(2) ). (E) Coordination with States The Secretary shall coordinate with relevant State fish and wildlife agencies in carrying out this paragraph, including by engaging with such agencies not later than 30 days after the date of a declaration of a major disaster or emergency by the President. (F) National guidance The Secretary, in consultation with the Secretary of the Interior, the Secretary of Commerce, and the Secretary of Agriculture, shall establish guidance to ensure consistent implementation of this paragraph across each district of the Corps of Engineers. .",
      "versionDate": "2025-12-12",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-08T15:09:59Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6693ih.xml"
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
      "title": "SALAMANDER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T05:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SALAMANDER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlining Authorizations for Listed At-risk Marine and Aquatic Natural Disaster Emergency Resources Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act to establish expedited permitting procedures for post-natural disaster recovery activities, incorporating interagency coordination and best management practices to ensure timely rebuilding while protecting endangered species, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T05:48:22Z"
    }
  ]
}
```
