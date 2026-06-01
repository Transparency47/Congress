# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1286?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1286
- Title: Calling for a trade policy that supports workers, consumers, independent farmers, small businesses, and the environment.
- Congress: 119
- Bill type: HRES
- Bill number: 1286
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-29T16:52:20Z
- Update date including text: 2026-05-29T16:52:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-05-14 - IntroReferral: Submitted in House
- Latest action: 2026-05-14: Submitted in House

## Actions

- 2026-05-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-05-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1286",
    "number": "1286",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Calling for a trade policy that supports workers, consumers, independent farmers, small businesses, and the environment.",
    "type": "HRES",
    "updateDate": "2026-05-29T16:52:20Z",
    "updateDateIncludingText": "2026-05-29T16:52:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-14",
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
      "actionCode": "1025",
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-05-14T14:00:05Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MI"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "OR"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NJ"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "OH"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "WI"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MO"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "VT"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "AZ"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MS"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "TX"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "VA"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MI"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "IL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NJ"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1286ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1286\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2026 Ms. DeLauro (for herself, Mrs. Dingell , Mr. Lynch , Mr. Deluzio , Mr. Khanna , Ms. Hoyle of Oregon , Ms. Waters , Mr. Riley of New York , Mr. Mrvan , Mr. Norcross , Mr. Boyle of Pennsylvania , Ms. Kaptur , Mr. Pocan , Ms. Schakowsky , Ms. Vel\u00e1zquez , Ms. Budzinski , Mr. Cleaver , Ms. Balint , Mrs. Grijalva , Mr. McGovern , Mr. Thompson of Mississippi , Ms. Ocasio-Cortez , Ms. Scanlon , Mr. Casar , Mr. Tonko , Mr. Scott of Virginia , Ms. Stevens , Mr. Morelle , and Mr. Garc\u00eda of Illinois ) submitted the following resolution; which was referred to the Committee on Ways and Means\nRESOLUTION\nCalling for a trade policy that supports workers, consumers, independent farmers, small businesses, and the environment.\nThat\u2014\n**(1)**\nthe House of Representatives rejects the choice between President Trump\u2019s chaotic, corrupt, corporate-captured trade policies and a return to the devastating trade model of the past;\n**(2)**\nthe House of Representatives supports a trade policy that unflaggingly centers workers, supports family farmers and consumers, promotes a healthy environment, and enhances national well-being, resilience, and security; and\n**(3)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\nto eliminate major incentives for companies to offshore jobs, any trade agreement must include strong, binding labor and environmental standards and rules of origin backed by swift and certain enforcement mechanisms;\n**(B)**\ntrade agreements must include effective tools for challenging violations, including at the facility level, and businesses and governments must be held accountable when they fail to uphold workers\u2019 rights and environmental protections;\n**(C)**\ntrade agreements must also include fair wage guarantees across manufacturing, food processing, call centers, back-office, and other tradeable sectors to disincentivize offshoring;\n**(D)**\nrobust development assistance funding, including the grant program administered by the Department of Labor\u2019s International Labor Affairs Bureau, should ensure that strong labor provisions level the playing field by improving respect for workers\u2019 rights;\n**(E)**\ncorporations seeking preferential tariff treatment must be required to meet a wage floor; and\n**(F)**\ntrade should raise wages and standards globally, not allow companies to seek out low-wage labor markets with weak workers\u2019 rights and environmental protections, pitting workers against each other in a never-ending race to the bottom;\n**(4)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\npublic procurement and infrastructure investment should support United States workers;\n**(B)**\ntrade agreements must in no way undermine governments\u2019 ability to\u2014\n**(i)**\npreference the purchase of domestic products at the Federal or State level; or\n**(ii)**\ninclude labor, environmental, and other standards in their purchasing preferences;\n**(C)**\ndomestically, Buy America requirements must be strengthened to ensure goods are truly made in the United States, not minimally assembled or routed through loopholes;\n**(D)**\nrules must be strengthened to ensure that products, such as steel and aluminum, are melted, poured, smelted, cast, and fabricated domestically; and\n**(E)**\nwaivers to such requirements and rules should be limited, and domestic content standards should apply across infrastructure, energy, and defense spending;\n**(5)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\nUnited States trade and tax policy must stop incentivizing companies to move production overseas and, instead, should penalize them for doing so;\n**(B)**\nUnited States trade agreements must include mechanisms for targeting individual cases of offshoring and should condition United States market access on the creation of good American jobs;\n**(C)**\nFederal contracts, tax incentives, and financing must prioritize companies that invest and produce in the United States, and should include clawbacks and other remedies against companies and their leaders that offshore jobs or supply chains;\n**(D)**\ntrade should rebuild domestic manufacturing capacity, not accelerate its decline, and must be complemented by robust industrial policies to support union jobs, with similar conditions and remedies to support workers; and\n**(E)**\nwhen trade policies fail to prevent offshoring, the United States must have an active, accessible, and fully funded Trade Adjustment Assistance Program to help workers get back on their feet;\n**(6)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\ntrade policy must not allow companies to undercut United States workers by exploiting weaker standards abroad;\n**(B)**\nUnited States trade agreements must include robust environmental standards, including those to limit industrial point water, air, climate, and ground pollution, that are enforced with effective mechanisms to challenge violations;\n**(C)**\nindustrial espionage, forced technology transfer, and intellectual property theft conducted to create unfair advantages over United States producers must be treated as trade violations and met with strong enforcement;\n**(D)**\nUnited States trade and investment agreements must exclude the investor-state dispute settlement system that incentivizes offshoring and threatens environmental, labor, and other public policies by granting special rights to transnational corporations; and\n**(E)**\ntrade should reward responsible production, not a race to the bottom;\n**(7)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\ntrade agreements should prioritize access to affordable medicine at home and abroad;\n**(B)**\ntrade policy must not constrain governments\u2019 ability to adopt policies that enable the domestic production of medicine to address public health needs and to negotiate with companies for lower prescription drug prices; and\n**(C)**\nUnited States trade agreements should not provide monopoly protections that enable pharmaceutical firms to raise drug prices;\n**(8)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\ntrade must prioritize benefits for independent and family farmers and rural communities, including through\u2014\n**(i)**\nmandatory country-of-origin labeling rules to ensure market transparency;\n**(ii)**\ndisciplines on subsidies that exclude large producers and processors but permit targeted support for small-, mid-, and family-scale farmers; and\n**(iii)**\nantimonopoly disciplines to promote fair input prices and farm gate prices; and\n**(B)**\ntrade agreements must also recognize countries\u2019 sovereignty to set their own food safety standards and related inspection standards;\n**(9)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\nmuch of the digital economy, including the training of artificial intelligence , is being built on the backs of exploited workers overseas and without regard to its multiple impacts here at home;\n**(B)**\ntrade agreements not only need robust worker\u2019s rights protections for the digital economy, but must in no way constrain countries\u2019 ability to set and enforce policy with respect to\u2014\n**(i)**\ndata privacy, security, and storage;\n**(ii)**\nright-to-repair policies;\n**(iii)**\nregulation of artificial intelligence;\n**(iv)**\nprotection against online discrimination and other civil rights violations;\n**(v)**\ncompetition in the marketplace; and\n**(vi)**\nrelated issues; and\n**(C)**\ntrade policy must also provide protections for the copyrighted work of the more than 5,000,000 people who work in the motion picture, television, and music industries;\n**(10)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\ntrade policies should not privilege corporations, whether through provisions included in trade agreements, special access to policymakers, or privileged positions in tariff and waiver discussions;\n**(B)**\nthe priorities of working families should be front and center in transparent negotiations, including when decisions are being made about food safety, environmental, health, privacy, labor, worker safety, and other standards; and\n**(C)**\nCongress must vote to approve any new or renegotiated trade or investment agreement that includes binding terms that change any existing or constrain any future United States policies;\n**(11)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\ntariffs are a critical tool to counter unfair trade and corporate greed and to strengthen strategic sectors;\n**(B)**\nthe United States must maintain and strengthen tariffs under section 232 of the Trade Expansion Act of 1962 ( 19 U.S.C. 1862 ) and section 301 of the Trade Act of 1974 ( 19 U.S.C. 2411 ) where they support domestic production and good-paying jobs;\n**(C)**\nwhen an Administration fails to maintain and strengthen such tariffs to support American industry and workers, Congress will exercise its constitutional trade authority to address specific abuses;\n**(D)**\nsuch tariffs should not be weakened or removed if doing so exposes workers to import surges or trade cheating; and\n**(E)**\nCongress opposes giving corporations and bad actors overseas a free pass; and\n**(12)**\nit is the sense of the House of Representatives that\u2014\n**(A)**\nthe United States must fully enforce its trade laws to stop other unfair practices, such as dumping and government-subsidized products on the United States market, to undercut United States producers;\n**(B)**\nantidumping and countervailing duty laws must be applied robustly and without delay;\n**(C)**\nexisting trade preference programs must be updated to close loopholes that allow companies to evade duties; and\n**(D)**\nenforcement agencies must be fully funded so they can act quickly and effectively to catch and prevent abuses.",
      "versionDate": "2026-05-14",
      "versionType": "IH"
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-05-29T16:52:20Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1286ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Calling for a trade policy that supports workers, consumers, independent farmers, small businesses, and the environment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:18:30Z"
    },
    {
      "title": "Calling for a trade policy that supports workers, consumers, independent farmers, small businesses, and the environment.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:07:36Z"
    }
  ]
}
```
