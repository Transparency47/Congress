# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/75?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/75
- Title: HOUSE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 75
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-02T14:50:19Z
- Update date including text: 2025-12-02T14:50:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/75",
    "number": "75",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "HOUSE Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-02T14:50:19Z",
    "updateDateIncludingText": "2025-12-02T14:50:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-06T17:41:36Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:08:30Z",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "LA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "MI"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr75ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 75\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Ogles , and Mr. Higgins of Louisiana ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Housing and Urban Development and the Secretary of Agriculture to withdraw a final determination relating to energy efficiency standards for housing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Owners with Unaffordable Shoddy Edicts Act of 2025 or the HOUSE Act of 2025 .\n#### 2. Energy efficiency standards for housing\n##### (a) In general\nThe Secretary of Housing and Urban Development and the Secretary of Agriculture\u2014\n**(1)**\nshall withdraw the final determination announced in the notice of final determination entitled Adoption of Energy Efficiency Standards for New Construction of HUD- and USDA-Financed Housing (89 Fed. Reg. 33112);\n**(2)**\nmay not take any action or use any Federal funds to implement or enforce the final determination described in paragraph (1) or any substantially similar final determination; and\n**(3)**\nshall revert energy efficiency standards for covered programs under such final determination to the energy efficiency standards required before such final determination.\n##### (b) Action by additional agencies\n**(1) Department of Veterans Affairs**\nThe Secretary of Veterans Affairs may not take any action or use any Federal funds to implement or enforce a final determination that is substantially similar to the final determination described in subsection (a)(1).\n**(2) Federal Housing Finance Agency**\nNotwithstanding any other provision of law, the Director of the Federal Housing Finance Agency may not finalize, implement, or enforce a determination or rule relating to energy efficiency standards for single and multifamily housing.\n##### (c) Consideration of State standards\nSection 109(d) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12709(d) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) not less than 26 States have adopted an energy efficiency code or standard that meets or exceeds the requirements of the revised code or standard. .",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-11-18",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S8206)"
      },
      "number": "3178",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to require the Secretary of Housing and Urban Development and the Secretary of Agriculture to withdraw a final determination relating to energy efficiency standards for housing, and for other purposes.",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-06-10T17:11:08Z"
          },
          {
            "name": "Building construction",
            "updateDate": "2025-06-10T17:14:18Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-10T17:11:41Z"
          },
          {
            "name": "Department of Housing and Urban Development",
            "updateDate": "2025-06-10T17:11:27Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2025-06-10T17:11:54Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-06-10T17:16:05Z"
          },
          {
            "name": "Housing industry and standards",
            "updateDate": "2025-06-10T17:15:24Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-06-10T17:15:40Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-06-10T17:15:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-02-04T12:22:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr75",
          "measure-number": "75",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr75v00",
            "update-date": "2025-04-16"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Helping Owners with\u00a0Unaffordable Shoddy Edicts Act of 2025 or the HOUSE Act of 2025</strong></p><p>This bill directs the Department of Housing and Urban Development (HUD) and the Department of Agriculture (USDA) to withdraw the final determination titled<em> Adoption of Energy Efficiency Standards for New Construction of HUD- and USDA-Financed Housing</em> and published on April 26, 2024.</p><p>The determination adopted updated minimum energy efficiency standards for newly built homes (except manufactured housing) financed through certain HUD and USDA programs. Specifically, it adopted the (1) 2021 International Energy Conservation Code (IECC), which\u00a0applies to single family homes and multifamily low-rise buildings up to three stories; and (2) 2019\u00a0American National Standards Institute/American Society of Heating, Refrigerating, and Air-Conditioning Engineers/Illuminating Electrical Society (ANSI/ASHRAE/IES) Standard 90.1, which\u00a0applies to multifamily residential buildings with four or more stories. HUD and USDA must also revert to using the energy efficiency standards required before the determination.</p><p>In addition, the bill prohibits HUD, USDA, and the Department of Veterans Affairs from taking actions or using federal funds to implement or enforce the determination or any substantially similar determination. It also prohibits the Federal Housing Finance Agency from finalizing, implementing, or enforcing a determination or rule relating to energy efficiency standards for single and multifamily housing.</p><p>Finally, the bill prohibits HUD and USDA from adopting updates to the IECC or ANSI/ASHRAE/IES Standard 90.1 in certain circumstances unless\u00a0at least 26 states have adopted codes or standards that meet or exceed the update's requirements.</p>"
        },
        "title": "HOUSE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr75.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Helping Owners with\u00a0Unaffordable Shoddy Edicts Act of 2025 or the HOUSE Act of 2025</strong></p><p>This bill directs the Department of Housing and Urban Development (HUD) and the Department of Agriculture (USDA) to withdraw the final determination titled<em> Adoption of Energy Efficiency Standards for New Construction of HUD- and USDA-Financed Housing</em> and published on April 26, 2024.</p><p>The determination adopted updated minimum energy efficiency standards for newly built homes (except manufactured housing) financed through certain HUD and USDA programs. Specifically, it adopted the (1) 2021 International Energy Conservation Code (IECC), which\u00a0applies to single family homes and multifamily low-rise buildings up to three stories; and (2) 2019\u00a0American National Standards Institute/American Society of Heating, Refrigerating, and Air-Conditioning Engineers/Illuminating Electrical Society (ANSI/ASHRAE/IES) Standard 90.1, which\u00a0applies to multifamily residential buildings with four or more stories. HUD and USDA must also revert to using the energy efficiency standards required before the determination.</p><p>In addition, the bill prohibits HUD, USDA, and the Department of Veterans Affairs from taking actions or using federal funds to implement or enforce the determination or any substantially similar determination. It also prohibits the Federal Housing Finance Agency from finalizing, implementing, or enforcing a determination or rule relating to energy efficiency standards for single and multifamily housing.</p><p>Finally, the bill prohibits HUD and USDA from adopting updates to the IECC or ANSI/ASHRAE/IES Standard 90.1 in certain circumstances unless\u00a0at least 26 states have adopted codes or standards that meet or exceed the update's requirements.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119hr75"
    },
    "title": "HOUSE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Helping Owners with\u00a0Unaffordable Shoddy Edicts Act of 2025 or the HOUSE Act of 2025</strong></p><p>This bill directs the Department of Housing and Urban Development (HUD) and the Department of Agriculture (USDA) to withdraw the final determination titled<em> Adoption of Energy Efficiency Standards for New Construction of HUD- and USDA-Financed Housing</em> and published on April 26, 2024.</p><p>The determination adopted updated minimum energy efficiency standards for newly built homes (except manufactured housing) financed through certain HUD and USDA programs. Specifically, it adopted the (1) 2021 International Energy Conservation Code (IECC), which\u00a0applies to single family homes and multifamily low-rise buildings up to three stories; and (2) 2019\u00a0American National Standards Institute/American Society of Heating, Refrigerating, and Air-Conditioning Engineers/Illuminating Electrical Society (ANSI/ASHRAE/IES) Standard 90.1, which\u00a0applies to multifamily residential buildings with four or more stories. HUD and USDA must also revert to using the energy efficiency standards required before the determination.</p><p>In addition, the bill prohibits HUD, USDA, and the Department of Veterans Affairs from taking actions or using federal funds to implement or enforce the determination or any substantially similar determination. It also prohibits the Federal Housing Finance Agency from finalizing, implementing, or enforcing a determination or rule relating to energy efficiency standards for single and multifamily housing.</p><p>Finally, the bill prohibits HUD and USDA from adopting updates to the IECC or ANSI/ASHRAE/IES Standard 90.1 in certain circumstances unless\u00a0at least 26 states have adopted codes or standards that meet or exceed the update's requirements.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119hr75"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr75ih.xml"
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
      "title": "HOUSE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOUSE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Owners with Unaffordable Shoddy Edicts Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Housing and Urban Development and the Secretary of Agriculture to withdraw a final determination relating to energy efficiency standards for housing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T07:48:40Z"
    }
  ]
}
```
