# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2860?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2860
- Title: Revitalizing America’s Offshore Critical Minerals Dominance Act
- Congress: 119
- Bill type: S
- Bill number: 2860
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2860",
    "number": "2860",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Revitalizing America\u2019s Offshore Critical Minerals Dominance Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T15:57:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:30Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AR"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TN"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2860is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2860\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Sheehy (for himself, Mr. Cotton , Mrs. Blackburn , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo unleash United States offshore critical minerals and resources, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Revitalizing America\u2019s Offshore Critical Minerals Dominance Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe United States has a core national security and economic interest in maintaining leadership in deep sea science and technology and seabed mineral resources;\n**(2)**\nthe United States faces unprecedented economic and national security challenges in securing reliable supplies of critical minerals independent of foreign adversary control;\n**(3)**\nvast offshore seabed areas hold critical minerals and energy resources;\n**(4)**\noffshore seabed resources are key to strengthening the economy of the United States, securing the energy future, and reducing dependence on foreign suppliers for critical minerals;\n**(5)**\nthe United States controls seabed mineral resources in 1 of the largest ocean areas of the world;\n**(6)**\nthe United States can, through the exercise of existing authorities and by establishing international partnerships, access potentially vast resources in seabed polymetallic nodules, other subsea geologic structures, and coastal deposits containing strategic minerals such as nickel, cobalt, copper, manganese, titanium, and rare earth elements, which are vital to the national security and economic prosperity of the United States;\n**(7)**\nthe United States must take immediate action to accelerate the responsible development of seabed mineral resources, quantify the endowment of seabed minerals of the United States, reinvigorate United States leadership in associated extraction and processing technologies, and ensure secure supply chains for the defense, infrastructure, and energy sectors of the United States; and\n**(8)**\nit is the policy of the United States to advance United States leadership in seabed mineral development by\u2014\n**(A)**\nrapidly developing domestic capabilities for the exploration, characterization, collection, and processing of seabed mineral resources through streamlined permitting without compromising environmental and transparency standards;\n**(B)**\nsupporting investment in deep sea science, mapping, and technology;\n**(C)**\nenhancing coordination among executive departments and agencies with respect to seabed mineral development activities described in this Act;\n**(D)**\nestablishing the United States as a global leader in responsible seabed mineral exploration, development technologies, and practices, and as a partner for countries developing seabed mineral resources in areas within their national jurisdictions, including their exclusive economic zones;\n**(E)**\ncreating a robust domestic supply chain for critical minerals derived from seabed mineral resources to support economic growth, reindustrialization, and military preparedness, including through new processing capabilities; and\n**(F)**\nstrengthening partnerships with allies and industry to counter the growing influence of China over seabed mineral resources, and to ensure that United States companies are well-positioned to support allies and partners interested in developing seabed minerals responsibly in areas within their national jurisdictions, including their exclusive economic zones.\n#### 3. Definitions\nIn this Act:\n**(1) Commercial recovery**\nThe term commercial recovery has the meaning given the term in section 4 of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1403 ).\n**(2) Critical mineral**\nThe term critical mineral has the meaning given the term in section 7002(a) of the Energy Act of 2020 ( 30 U.S.C. 1606(a) ).\n**(3) Exploration**\nThe term exploration has the meaning given the term in section 4 of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1403 ).\n**(4) Lease**\nThe term lease has the meaning given the term in section 2 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 ).\n**(5) Mineral**\nThe term mineral means\u2014\n**(A)**\na critical mineral;\n**(B)**\nuranium;\n**(C)**\ncopper;\n**(D)**\npotash;\n**(E)**\ngold; and\n**(F)**\nany other element or compound that the Chair of the National Energy Dominance Council determines appropriate.\n**(6) Outer Continental Shelf**\nThe term outer Continental Shelf has the meaning given the term in section 2 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 ).\n**(7) Processing**\nThe term processing includes the concentration, separation, refinement, alloying, and conversion of minerals into usable forms.\n**(8) Prospecting**\nThe term prospecting has the meaning given the term geological and geophysical (G&G) prospecting activities in section 580.1 of title 30, Code of Federal Regulations (or a successor regulation).\n**(9) Seabed mineral resource**\nThe term seabed mineral resource means a mineral-bearing material located in the seabed of the outer Continental Shelf, including\u2014\n**(A)**\na polymetallic nodule;\n**(B)**\na cobalt-rich ferromanganese crust;\n**(C)**\na polymetallic sulfide;\n**(D)**\na heavy mineral sand; and\n**(E)**\na phosphorite.\n**(10) United States company**\nThe term United States company has the meaning given the term United States citizen in section 4 of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1403 ).\n#### 4. Strategic seabed critical mineral access\n##### (a) Expediting issuance of certain authorizations\n**(1) Deep Seabed Hard Mineral Resources Act**\nNot later than 60 days after the date of enactment of this Act, the Secretary of Commerce, acting through the Administrator of the National Oceanic and Atmospheric Administration, in consultation with the Secretary of State and Secretary of the Interior, acting through the Director of the Bureau of Ocean Energy Management, shall\u2014\n**(A)**\nexpedite the process for reviewing and issuing licenses for exploration and permits for commercial recovery under the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1401 et seq. ); and\n**(B)**\ncarry out subparagraph (A) in a manner ensuring efficiency, predictability, and competitiveness for United States companies.\n**(2) Outer Continental Shelf Lands Act**\nNot later than 60 days after the date of enactment of this Act, the Secretary of the Interior shall\u2014\n**(A)**\nestablish an expedited process for reviewing and approving permits for prospecting and granting leases under the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 et seq. ); and\n**(B)**\ncarry out subparagraph (A) in a manner ensuring efficiency, predictability, and competitiveness for United States companies.\n##### (b) Seabed mapping plan\nNot later than 60 days after the date of enactment of this Act, the Secretary of the Interior, in consultation with the Secretary of State, the Secretary of Commerce, and the heads of other relevant Federal departments and agencies, and in cooperation with commercial and other nongovernmental organizations, shall develop a plan to map priority areas of the seabed and outer Continental Shelf of the United States, to include extended areas of the outer Continental Shelf, such as those with abundant or accessible seabed mineral resources, to accelerate data collection and characterization.\n##### (c) Identification of certain critical minerals\nNot later than 60 days after the date of enactment of this Act, the Secretary of the Interior shall\u2014\n**(1)**\nidentify critical minerals that may be derived from seabed mineral resources; and\n**(2)**\nin coordination with the Secretary of Defense and Secretary of Energy, determine which critical minerals derived from seabed mineral resources are essential for applications such as defense infrastructure, manufacturing, and energy.\n##### (d) Engagement with key partners and allies\n**(1) In general**\nNot later than 60 days after the date of enactment of this Act, the Secretary of Commerce, in coordination with the Secretary of State, Secretary of the Interior, and Secretary of Energy, shall engage with key partners and allies to offer support for seabed mineral resource exploration, extraction, processing, and environmental monitoring in areas within the jurisdictions of such key partners and allies, including by\u2014\n**(A)**\nseeking scientific collaboration and commercial development opportunities for United States companies; and\n**(B)**\ndeveloping a prioritized list of foreign countries for engagement.\n**(2) Key partner or ally determination**\n**(A) In general**\nThe Secretary of State shall determine whether an entity is a key partner or ally for the purposes of paragraph (1) based on several factors, including\u2014\n**(i)**\nexisting agreements with the United States;\n**(ii)**\nalignment with strategic interests of the United States; and\n**(iii)**\nparticipation in joint initiatives.\n**(B) Notification**\nThe Secretary of State shall notify the Secretary of Commerce, Secretary of the Interior, and Secretary of Energy of any determination made under subparagraph (A).\n##### (e) Reports\nNot later than 60 days after the date of enactment of this Act\u2014\n**(1)**\nthe Secretary of the Interior, in coordination with the Secretary of Commerce and Secretary of Energy, and in consultation with the heads of other relevant Federal departments and agencies, shall submit to the Committees on Energy and Natural Resources and Commerce, Science, and Transportation of the Senate and the Committee on Natural Resources of the House of Representatives a report that identifies private sector interest in and opportunities for seabed mineral resource exploration and mining on the outer Continental Shelf, in areas beyond national jurisdiction, and in areas within the jurisdiction of a foreign country that expresses interest in partnering with United States companies with respect to seabed mineral resource development; and\n**(2)**\nthe Secretary of the Interior, jointly with the Secretary of State, Secretary of Commerce, and Secretary of Energy, shall submit to the Committees on Energy and Natural Resources and Commerce, Science, and Transportation of the Senate and the Committee on Natural Resources of the House of Representatives a report regarding the feasibility of an international benefit-sharing mechanism for seabed mineral resource extraction and development that occurs in an area beyond the jurisdiction of any country.\n##### (f) Rules of construction\nNothing in this Act\u2014\n**(1)**\nimpairs or otherwise affects the authority granted by law to any executive department or agency; or\n**(2)**\ncreates any right or benefit, substantive or procedural, enforceable at law or in equity by any party against the United States, any department, agency, or entity of the United States, any officer, employee, or agent of the United States, or any other person.",
      "versionDate": "2025-09-18",
      "versionType": "Introduced in Senate"
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
            "name": "Alliances",
            "updateDate": "2026-02-19T19:36:49Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2026-02-19T19:36:49Z"
          },
          {
            "name": "Metals",
            "updateDate": "2026-02-19T19:36:49Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-02-19T19:36:49Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-02-19T19:36:49Z"
          },
          {
            "name": "Seashores and lakeshores",
            "updateDate": "2026-02-19T19:36:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-12-17T16:24:23Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2860is.xml"
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
      "title": "Revitalizing America\u2019s Offshore Critical Minerals Dominance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Revitalizing America\u2019s Offshore Critical Minerals Dominance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to unleash United States offshore critical minerals and resources, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:15Z"
    }
  ]
}
```
