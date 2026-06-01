# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/834?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/834
- Title: Disaster Assistance Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 834
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-05-11T20:45:26Z
- Update date including text: 2026-05-11T20:45:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/834",
    "number": "834",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Disaster Assistance Fairness Act",
    "type": "HR",
    "updateDate": "2026-05-11T20:45:26Z",
    "updateDateIncludingText": "2026-05-11T20:45:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-01",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:09:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-01T15:43:49Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CO"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "DC"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CO"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr834ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 834\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Rouzer (for himself, Mr. Torres of New York , Mr. Nadler , and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide assistance for common interest communities, condominiums, and housing cooperatives damaged by a major disaster, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Assistance Fairness Act .\n#### 2. Definitions\nSection 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ) is amended by adding at the end the following:\n(13) Residential common interest community The term residential common interest community means any nonprofit mandatory membership organization comprising owners of real estate described in a declaration or created pursuant to a covenant or other applicable law with respect to which a person, by virtue of the person\u2019s ownership of a unit, is obligated to pay for a share of real estate taxes, insurance premiums, maintenance, or improvement of, or services or other expenses related to, common elements, other units, or any other real estate other than that unit described in the declaration. (14) Condominium The term condominium means a multi-unit housing project in which each dwelling unit is separately owned, and the remaining portions of the real estate are designated for common ownership solely by the owners of those units, each owner having an undivided interest in the common elements, and which is represented by a condominium association consisting exclusively of all the unit owners in the project, which is, or will be responsible for the operation, administration, and management of the project. (15) Housing cooperative The term housing cooperative means a multi-unit housing entity in which each dwelling unit is subject to separate use and possession by 1 or more cooperative members whose interest in such unit, and in any undivided assets of the cooperative association that are appurtenant to such unit, is evidenced by a membership or share interest in a cooperative association and a lease or other document of title or possession granted by such cooperative as the owner of all cooperative property. (16) Manufactured housing community The term manufactured housing community means a residential development or neighborhood specifically designed for the placement of manufactured homes, as that term is defined in 24 C.F.R. 3280.02, modular homes, prefabricated homes, or any combination of each. .\n#### 3. Removal of debris resulting from a major disaster in residential common interest communities\nSection 407 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5173 ) is amended\u2014\n**(1)**\nby redesignating subsections (d) and (e) as subsections (e) and (f); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Rules relating to residential common interest communities The President shall issue rules which provide that removal of debris or wreckage from real estate owned by a residential common interest community, condominium entity, manufactured housing community, or housing cooperative resulting from a major disaster is in the public interest when a State or local government determines in writing such debris or wreckage constitutes a threat to life, to public health or safety, or to the economic recovery of the residential common interest community. .\n#### 4. Condominiums, manufactured housing communities, and housing cooperatives damaged by a major disaster\nSection 408(c)(2)(A) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174(c)(2)(A) ) is amended\u2014\n**(1)**\nin clause (i) by striking and at the end;\n**(2)**\nby redesignating clause (ii) as clause (iii); and\n**(3)**\nby adding after clause (i) the following:\n(ii) the repair of essential common elements of a condominium, manufactured housing community, or housing cooperative (such as a roof, exterior wall, heating and cooling equipment, elevator, stairwell, utility access, plumbing, and electricity) provided an individual\u2019s or household\u2019s pro rata share of essential common element repair costs are satisfactorily documented; and .\n#### 5. Applicability\nThe amendments made by this Act shall apply to a major disaster or emergency declared by the President under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ) on or after the date of enactment of this Act.",
      "versionDate": "2025-01-31",
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
        "name": "Emergency Management",
        "updateDate": "2025-03-31T14:42:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr834",
          "measure-number": "834",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2026-05-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr834v00",
            "update-date": "2026-05-11"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Disaster Assistance </strong><strong>Fairness Act</strong></p><p>This bill makes common interest communities, such as housing cooperatives (co-ops) and condominiums, and manufactured housing communities eligible for the same assistance from the Federal Emergency Management Agency (FEMA) as other homeowners.</p><p>Specifically, the bill</p><ul><li>adds definitions of <em>residential common interest community, condominium, housing cooperative, </em>and<em> manufactured housing community</em> to the Robert T. Stafford Disaster Relief and Emergency Assistance Act;</li><li>requires FEMA to issue rules for the removal of debris or wreckage from real estate owned by a residential common interest community,\u00a0condominium, co-op, or manufactured housing community resulting from a major disaster and deems such removal to be in the public interest when a state or local government determines in writing that such debris or wreckage constitutes a threat to life, public health or safety, or the economic recovery of such community; and</li><li>provides for the repair of essential common elements of a condominium, co-op, or manufactured housing community damaged\u00a0by a disaster under FEMA's Individuals and Households Program.</li></ul>"
        },
        "title": "Disaster Assistance Fairness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr834.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disaster Assistance </strong><strong>Fairness Act</strong></p><p>This bill makes common interest communities, such as housing cooperatives (co-ops) and condominiums, and manufactured housing communities eligible for the same assistance from the Federal Emergency Management Agency (FEMA) as other homeowners.</p><p>Specifically, the bill</p><ul><li>adds definitions of <em>residential common interest community, condominium, housing cooperative, </em>and<em> manufactured housing community</em> to the Robert T. Stafford Disaster Relief and Emergency Assistance Act;</li><li>requires FEMA to issue rules for the removal of debris or wreckage from real estate owned by a residential common interest community,\u00a0condominium, co-op, or manufactured housing community resulting from a major disaster and deems such removal to be in the public interest when a state or local government determines in writing that such debris or wreckage constitutes a threat to life, public health or safety, or the economic recovery of such community; and</li><li>provides for the repair of essential common elements of a condominium, co-op, or manufactured housing community damaged\u00a0by a disaster under FEMA's Individuals and Households Program.</li></ul>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr834"
    },
    "title": "Disaster Assistance Fairness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disaster Assistance </strong><strong>Fairness Act</strong></p><p>This bill makes common interest communities, such as housing cooperatives (co-ops) and condominiums, and manufactured housing communities eligible for the same assistance from the Federal Emergency Management Agency (FEMA) as other homeowners.</p><p>Specifically, the bill</p><ul><li>adds definitions of <em>residential common interest community, condominium, housing cooperative, </em>and<em> manufactured housing community</em> to the Robert T. Stafford Disaster Relief and Emergency Assistance Act;</li><li>requires FEMA to issue rules for the removal of debris or wreckage from real estate owned by a residential common interest community,\u00a0condominium, co-op, or manufactured housing community resulting from a major disaster and deems such removal to be in the public interest when a state or local government determines in writing that such debris or wreckage constitutes a threat to life, public health or safety, or the economic recovery of such community; and</li><li>provides for the repair of essential common elements of a condominium, co-op, or manufactured housing community damaged\u00a0by a disaster under FEMA's Individuals and Households Program.</li></ul>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr834"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr834ih.xml"
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
      "title": "Disaster Assistance Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disaster Assistance Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide assistance for common interest communities, condominiums, and housing cooperatives damaged by a major disaster, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T05:18:34Z"
    }
  ]
}
```
