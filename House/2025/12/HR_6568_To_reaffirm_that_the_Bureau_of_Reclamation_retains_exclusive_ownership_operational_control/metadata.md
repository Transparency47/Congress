# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6568?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6568
- Title: Lower Yellowstone River Native Fish Conservation Act
- Congress: 119
- Bill type: HR
- Bill number: 6568
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-02-17T20:04:29Z
- Update date including text: 2026-02-17T20:04:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-28 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-02-04 - Committee: Subcommittee Hearings Held
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-28 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-02-04 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6568",
    "number": "6568",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Lower Yellowstone River Native Fish Conservation Act",
    "type": "HR",
    "updateDate": "2026-02-17T20:04:29Z",
    "updateDateIncludingText": "2026-02-17T20:04:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-28",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-04T15:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-28T18:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6568ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6568\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Downing introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo reaffirm that the Bureau of Reclamation retains exclusive ownership, operational control, and financial responsibility for the Lower Yellowstone Fish Bypass Channel, ensuring long-term conservation of the endangered pallid sturgeon and other native aquatic species in the Yellowstone River while protecting the Lower Yellowstone Irrigation Project and District from undue financial and operational burdens, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lower Yellowstone River Native Fish Conservation Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe Lower Yellowstone Fish Bypass Channel\u2014\n**(A)**\nwas authorized under section 3109 of the Water Resources Development Act of 2007 ( Public Law 110\u2013114 ; 121 Stat. 1135) as a Federal mitigation measure for impacts on the pallid sturgeon (Scaphirhynchus albus) under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. );\n**(B)**\nwas designed and constructed by the Corps of Engineers and the Bureau of Reclamation using funds from the Missouri River Recovery Program and other Federal appropriations specifically allocated for ecosystem restoration and endangered species mitigation; and\n**(C)**\nis located outside the physical and operational boundaries of the Lower Yellowstone Irrigation Project and the Lower Yellowstone Irrigation District;\n**(2)**\nthe Bureau of Reclamation retains sole ownership, operational jurisdiction, and maintenance responsibilities for the Lower Yellowstone Fish Bypass Channel and related infrastructure;\n**(3)**\nthe Lower Yellowstone Irrigation Project was federally authorized in 1904 under the Act of June 17, 1902 (32 Stat. 388, chapter 1093), to provide irrigation water to agricultural land in eastern Montana and western North Dakota;\n**(4)**\nthe Lower Yellowstone Irrigation District, established under Montana and North Dakota State laws, has never had ownership, operational responsibility, or maintenance obligations relating to the Lower Yellowstone Fish Bypass Channel;\n**(5)**\nthe Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) mandates Federal protection and recovery actions for listed species, including the pallid sturgeon (Scaphirhynchus albus);\n**(6)**\nendangered species recovery, including construction of the Lower Yellowstone Fish Bypass Channel, is solely a Federal responsibility;\n**(7)**\nthe Bureau of Reclamation opted to construct the Lower Yellowstone Fish Bypass Channel to comply with the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) because the Intake Diversion Dam is federally owned and operated, rather than owned or operated by the Lower Yellowstone Irrigation District or the Lower Yellowstone Irrigation Project;\n**(8)**\nthe Lower Yellowstone Irrigation District or the Lower Yellowstone Irrigation Project cannot and should not be burdened with financial or operational responsibility for a federally mandated environmental mitigation project;\n**(9)**\nthe Lower Yellowstone Fish Bypass Channel is legally separate and distinct from the Lower Yellowstone Irrigation Project and the Lower Yellowstone Irrigation District; and\n**(10)**\nwithout legislative clarity, future administrative actions could inappropriately attempt to shift the burden of operations and maintenance costs of the Lower Yellowstone Fish Bypass Channel onto the Lower Yellowstone Irrigation District, which is a scenario that contradicts the original intent of the authorization for the Lower Yellowstone Fish Bypass Channel under the Water Resources Development Act of 2007 ( Public Law 110\u2013114 ; 121 Stat. 1041).\n#### 3. Definitions\nIn this Act:\n**(1) Lower Yellowstone Fish Bypass Channel**\nThe term Lower Yellowstone Fish Bypass Channel means the 2.1-mile-long engineered fish passage channel constructed near Intake, Montana, designed to facilitate the migration of pallid sturgeon (Scaphirhynchus albus) and other native fish species around the Intake Diversion Dam located near Intake, Montana.\n**(2) Lower Yellowstone Irrigation District**\nThe term Lower Yellowstone Irrigation District means the local, State-chartered water management entity responsible for operating and maintaining the irrigation components of the Lower Yellowstone Irrigation Project.\n**(3) Lower Yellowstone Irrigation Project**\nThe term Lower Yellowstone Irrigation Project means the Federal irrigation system\u2014\n**(A)**\nauthorized in 1904 under the Act of June 17, 1902 (32 Stat. 388, chapter 1093); and\n**(B)**\noperated in partnership with the Lower Yellowstone Irrigation District for agricultural water delivery.\n**(4) Operations and maintenance**\nThe term operations and maintenance means all actions, costs, and labor necessary to operate, repair, upgrade, and maintain the Lower Yellowstone Fish Bypass Channel.\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Commissioner of Reclamation.\n#### 4. Reaffirmation of Federal ownership and responsibility\n##### (a) Sole ownership and control\n**(1) In general**\nThe Secretary shall retain full ownership, operational authority, and financial responsibility for the Lower Yellowstone Fish Bypass Channel in perpetuity.\n**(2) Administrative actions, agreements, or transfers**\nNo administrative action, agreement, or transfer shall alter, diminish, or delegate to any non-Federal entity, including the Lower Yellowstone Irrigation District or the Lower Yellowstone Irrigation Project, the responsibilities and authorities described in paragraph (1) with respect to the Lower Yellowstone Fish Bypass Channel.\n**(3) Effect**\nNothing in this Act prevents the Secretary from retaining the authority to enter into agreements with, coordinate, or otherwise work with the head of any other Federal agency, including with respect to funding, planning, or implementation of activities authorized under this Act or any other Act.\n##### (b) Operation and maintenance obligations\nThe Secretary shall be solely responsible for funding, operating, and maintaining the Lower Yellowstone Fish Bypass Channel, including any repairs, modifications, or adaptive management strategies.\n##### (c) Prohibition of cost transfer\nNo Federal agency may impose, mandate, or require the Lower Yellowstone Irrigation District, the Lower Yellowstone Irrigation Project, or any other non-Federal entity to assume financial or operational responsibility for any aspect of the Lower Yellowstone Fish Bypass Channel.\n##### (d) Relationship to the Lower Yellowstone Irrigation District or the Lower Yellowstone Irrigation Project\nNothing in this Act alters, amends, or otherwise affects the authorized purposes, water delivery obligations, or operational responsibilities of the Lower Yellowstone Irrigation District or the Lower Yellowstone Irrigation Project.\n#### 5. Preservation of Endangered Species Act obligations\n##### (a) Federal responsibility for pallid sturgeon recovery\n**(1) In general**\nThe Secretary and the Director of the United States Fish and Wildlife Service shall retain exclusive responsibility for fulfilling obligations relating to the pallid sturgeon (Scaphirhynchus albus) under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) with respect to the Lower Yellowstone Fish Bypass Channel.\n**(2) No obligation on the Lower Yellowstone Irrigation District or the Lower Yellowstone Irrigation Project**\nThe Lower Yellowstone Irrigation District and the Lower Yellowstone Irrigation Project shall not be required to perform, fund, or participate in any activities mandated under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) relating to the Lower Yellowstone Fish Bypass Channel or pallid sturgeon (Scaphirhynchus albus) conservation associated with the Lower Yellowstone Fish Bypass Channel.\n##### (b) Coordination with State and Federal Agencies\nThe Secretary shall coordinate with Montana Fish, Wildlife and Parks, the North Dakota Game and Fish Department, the United States Fish and Wildlife Service, and other relevant agencies to ensure proper conservation measures for the pallid sturgeon (Scaphirhynchus albus) without burdening private or local irrigation operations.\n#### 6. Prohibition of transfer of responsibilities\n##### (a) Limitation on transfer or delegation\n**(1) In general**\nThe Secretary shall not transfer, delegate, or assign any financial, operational, or maintenance responsibilities for the Lower Yellowstone Fish Bypass Channel to any non-Federal entity, including\u2014\n**(A)**\nthe Lower Yellowstone Irrigation District;\n**(B)**\nthe Lower Yellowstone Irrigation Project; and\n**(C)**\nany State agency, local government, or private entity.\n**(2) Clarification**\nNo agreement, contract, or memorandum of understanding shall have the effect of transferring to the Lower Yellowstone Irrigation District, the Lower Yellowstone Irrigation Project, or any other non-Federal entity the ownership of, responsibility for, or cost burden of the Lower Yellowstone Fish Bypass Channel.\n##### (b) Invalidation of prior attempts To transfer responsibility\n**(1) In general**\nAny prior administrative action, agreement, or cost-sharing arrangement that attempts to impose financial or operational responsibility for the Lower Yellowstone Fish Bypass Channel on the Lower Yellowstone Irrigation District or the Lower Yellowstone Irrigation Project shall be null and void.\n**(2) Termination of agreements**\nThe Secretary shall terminate any provision of any agreement that is inconsistent with this Act.\n#### 7. Legal enforcement and judicial review\n##### (a) Right To petition for Federal compliance\nThe Lower Yellowstone Irrigation District, the Lower Yellowstone Irrigation Project, and any affected stakeholder may file a complaint in Federal District Court seeking a declaratory judgment or other appropriate relief if the Secretary attempts to transfer to a non-Federal entity operational or financial responsibility for the Lower Yellowstone Fish Bypass Channel.\n##### (b) Jurisdiction\nThe United States District Court for the District of Montana shall have exclusive jurisdiction over any dispute arising under this Act.\n##### (c) No private cause of action against non-Federal entities\nNothing in this Act creates a private cause of action against the Lower Yellowstone Irrigation District, the Lower Yellowstone Irrigation Project, or any other non-Federal entity with respect to the operations and maintenance of the Lower Yellowstone Fish Bypass Channel.\n#### 8. Long-term Federal funding and resource allocation\n##### (a) Ongoing Federal responsibility for operations and maintenance\n**(1) In general**\nThe Secretary shall be the sole entity responsible for operations and maintenance and repairs of the Lower Yellowstone Fish Bypass Channel.\n**(2) Funding**\nThe Secretary shall fund all necessary repairs, modifications, and infrastructure improvements to maintain the effectiveness of the Lower Yellowstone Fish Bypass Channel.\n**(3) No financial burden**\nThe Lower Yellowstone Irrigation District, the Lower Yellowstone Irrigation Project, and any other non-Federal entity shall not bear any financial burden for maintenance, repairs, or monitoring of the Lower Yellowstone Fish Bypass Channel.\n##### (b) Authorization of appropriations\n**(1) In General**\nThere is authorized to be appropriated to the Secretary $1,000,000 for fiscal year 2026 and each fiscal year thereafter\u2014\n**(A)**\nto ensure continuous, uninterrupted operation of the Lower Yellowstone Fish Bypass Channel;\n**(B)**\nto conduct necessary engineering evaluations, repairs, and upgrades in the Lower Yellowstone Fish Bypass Channel as part of an ongoing Federal commitment to the Lower Yellowstone Fish Bypass Channel; and\n**(C)**\nto implement adaptive management strategies in the Lower Yellowstone Fish Bypass Channel to address environmental, hydrological, and biological changes affecting pallid sturgeon (Scaphirhynchus albus) passage.\n**(2) Administration of funds**\nThe Secretary\u2014\n**(A)**\nshall administer the funds made available under paragraph (1); and\n**(B)**\nmay not transfer or delegate to any non-Federal entity the funds made available under that paragraph.\n##### (c) Reporting requirement\nThe Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives a biennial report describing\u2014\n**(1)**\nthe operational status of the Lower Yellowstone Fish Bypass Channel;\n**(2)**\nany ongoing or anticipated repairs, modifications, or adaptive management actions with respect to the Lower Yellowstone Fish Bypass Channel;\n**(3)**\nan updated cost analysis of operations and maintenance of the Lower Yellowstone Fish Bypass Channel; and\n**(4)**\ncoordination efforts between the Secretary, the Director of the United States Fish and Wildlife Service, the Chief of Engineers, and State agencies with respect to the Lower Yellowstone Fish Bypass Channel.\n#### 9. Effect\nNothing in this Act\u2014\n**(1)**\nmodifies or diminishes the authorized purposes of the Lower Yellowstone Irrigation Project or the Lower Yellowstone Irrigation District;\n**(2)**\naffects any existing water rights of, or contracts or agreements between, the Secretary and the Lower Yellowstone Irrigation District or the Lower Yellowstone Irrigation Project;\n**(3)**\nimposes any new regulatory obligations, requirements, or liabilities on the Lower Yellowstone Irrigation District, the Lower Yellowstone Irrigation Project, or any other non-Federal entity;\n**(4)**\nmodifies or impairs State water law or any existing agreements relating to water distribution and irrigation operations; or\n**(5)**\nalters the statutory and regulatory obligations of Federal agencies under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) or the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-12-09",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "3409",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Lower Yellowstone River Native Fish Conservation Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-02-17T20:04:24Z"
          },
          {
            "name": "Endangered and threatened species",
            "updateDate": "2026-02-17T20:04:18Z"
          },
          {
            "name": "Fishes",
            "updateDate": "2026-02-17T20:03:51Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2026-02-17T20:04:29Z"
          },
          {
            "name": "Missouri River",
            "updateDate": "2026-02-17T20:04:02Z"
          },
          {
            "name": "Montana",
            "updateDate": "2026-02-17T20:04:07Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-02-17T20:04:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-01-07T23:06:46Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6568ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reaffirm that the Bureau of Reclamation retains exclusive ownership, operational control, and financial responsibility for the Lower Yellowstone Fish Bypass Channel, ensuring long-term conservation of the endangered pallid sturgeon and other native aquatic species in the Yellowstone River while protecting the Lower Yellowstone Irrigation Project and District from undue financial and operational burdens, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:21Z"
    },
    {
      "title": "Lower Yellowstone River Native Fish Conservation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lower Yellowstone River Native Fish Conservation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:20Z"
    }
  ]
}
```
