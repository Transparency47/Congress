# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2424?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2424
- Title: Modern, Clean, and Safe Trucks Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2424
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-05-30T08:05:51Z
- Update date including text: 2026-05-30T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-04-30 11:15:03 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. LaHood asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 2424, a bill originally introduced by Representative LaMalfa, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-04-30 11:15:03 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. LaHood asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 2424, a bill originally introduced by Representative LaMalfa, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2424",
    "number": "2424",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000578",
        "district": "1",
        "firstName": "Doug",
        "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
        "lastName": "LaMalfa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Modern, Clean, and Safe Trucks Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:51Z",
    "updateDateIncludingText": "2026-05-30T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2026-04-30",
      "actionTime": "11:15:03",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "ASSUMING FIRST SPONSORSHIP - Mr. LaHood asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 2424, a bill originally introduced by Representative LaMalfa, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:04:30Z",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NH"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NY"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "CO"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MN"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NC"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2424ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2424\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. LaMalfa (for himself, Mr. Pappas , Mr. LaHood , Mr. Carbajal , and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the excise tax on heavy trucks and trailers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modern, Clean, and Safe Trucks Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe 12-percent Federal retail excise tax on all new heavy trucks, tractors, and trailers, coupled with new regulatory mandates, significantly increases the cost of new heavy-duty trucks, tractors, and trailers and discourages the replacement of older, less environmentally clean and less fuel economical vehicles;\n**(2)**\nthis 12-percent Federal retail excise tax is the highest percentage rate of any Federal ad valorem excise tax;\n**(3)**\nthe Federal excise tax was first levied by Congress in 1917 to help finance America's involvement in World War I;\n**(4)**\nthe 12-percent Federal retail excise tax adds $7,000 or more to the cost of new trailers, $20,000 or more for new clean diesel trucks, and as much as $50,000 to the next generation of trucks with advanced engine technologies;\n**(5)**\nnearly half of the Class 8 trucks on the road are over 10 years old and lack a decade of environmental and safety technological advancements;\n**(6)**\nfrom 2007 to 2020, new trucks have reduced carbon dioxide emissions by 202,000,000 tons, nitrogen oxide emissions by 27,000,000 tons, and saved 20,000,000,000 gallons of diesel and 472,000,000 barrels of crude oil;\n**(7)**\nan owner of a single Class 8 truck powered by the latest clean diesel engine can expect to save about 2,200 gallons of fuel each year compared to previous generations of technology;\n**(8)**\nsince the late 1990s, cleaner fuel and advanced engines have combined to reduce nitrogen oxide (NO x ) emissions and particulate matter (PM) emissions by 98 percent;\n**(9)**\n60 trucks manufactured today emit the same amount as 1 truck manufactured in 1988;\n**(10)**\nthe Federal excise tax disproportionately impacts electric and alternative-fueled trucks, which currently have a higher up front cost, at a time when adoption of these technologies is needed to accelerate the transition to zero emission vehicles and the reduction of carbon pollution from transportation;\n**(11)**\nin 2020, there were approximately 1,300,000 United States manufacturing, supplier, dealership, and heavy-duty trucking and trailer related jobs;\n**(12)**\nsince the Federal retail excise tax on certain new heavy trucks, tractors, and trailers is based on annual sales, receipts from the tax deposited in the Highway Trust Fund can vary greatly;\n**(13)**\nCongress should consider a more reliable and consistent revenue mechanism to fund the Highway Trust Fund;\n**(14)**\nCongress should advance the deployment of the most modern, clean, and safe trucks through eliminating the Federal excise tax on trucks; and\n**(15)**\nrepealing the Federal excise tax would result in the replacement of older internal combustion engine trucks with new heavy duty trucks that employ the latest safety and environmental technologies.\n#### 3. Repeal of excise tax on heavy trucks and trailers\n##### (a) In general\nChapter 31 of the Internal Revenue Code of 1986 is amended by striking subchapter C (and by striking the item relating to such subchapter from the table of subchapters for such chapter).\n##### (b) Conforming amendments\n**(1)**\nSection 4072(c) of such Code is amended to read as follows:\n(c) Tires of the type used on highway vehicles (1) In general For purposes of this part, the term tires of the type used on highway vehicles means tires of the type used on\u2014 (A) motor vehicles which are highway vehicles, or (B) vehicles of the type used in connection with motor vehicles which are highway vehicles. (2) Exception for mobile machinery (A) In general Such term shall not include tires of a type used exclusively on mobile machinery. (B) Mobile machinery For purposes of subparagraph (A), the term mobile machinery means any vehicle which consists of a chassis\u2014 (i) to which there has been permanently mounted (by welding, bolting, riveting, or other means) machinery or equipment to perform a construction, manufacturing, processing, farming, mining, drilling, timbering, or similar operation if the operation of the machinery or equipment is unrelated to transportation on or off the public highways, (ii) which has been specially designed to serve only as a mobile carriage and mount (and a power source, where applicable) for the particular machinery or equipment involved, whether or not such machinery or equipment is in operation, and (iii) which, by reason of such special design, could not, without substantial structural modification, be used as a component of a vehicle designed to perform a function of transporting any load other than that particular machinery or equipment or similar machinery or equipment requiring such a specially designed chassis. .\n**(2)**\nSection 4221 of such Code is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking (or under subchapter C of chapter 31 on the first retail sale) , and\n**(ii)**\nby striking 4051 or ,\n**(B)**\nin subsection (c), by striking and in the case of any article sold free of tax under section 4053(6), , and\n**(C)**\nin subsection (d)(1), by striking , and, in the case of the taxes imposed by subchapter C of chapter 31, includes the retailer with respect to the first retail sale .\n**(3)**\nSection 4222(d) of such Code is amended by striking 4053(6), .\n**(4)**\nSection 4293 of such Code is amended by striking section 4051, .\n**(5)**\nSection 4483(g) of such Code is amended by striking section 4053(8) and inserting section 4072(c)(2) .\n**(6)**\nSection 6416(b)(2) of such Code is amended by striking or under section 4051 .\n**(7)**\nSection 6416(b) of such Code is amended by striking paragraph (6).\n**(8)**\nSection 9503(b)(1) of such Code is amended by striking subparagraph (B) and by redesignating subparagraphs (C), (D), and (E) as subparagraphs (B), (C), and (D), respectively.\n##### (c) Effective date\nThe amendments made by this section shall apply to sales and installations on or after the date of the introduction of this Act.",
      "versionDate": "2025-03-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Motor carriers",
            "updateDate": "2026-05-06T15:25:59Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-05-06T15:26:10Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2026-05-06T15:27:47Z"
          },
          {
            "name": "Sales and excise taxes",
            "updateDate": "2026-05-06T15:26:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-09T13:56:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119hr2424",
          "measure-number": "2424",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2026-02-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2424v00",
            "update-date": "2026-02-17"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong> Modern, Clean, and Safe Trucks Act of 2025</strong></p><p>This bill repeals the 12% federal excise tax imposed on the first retail sale of certain heavy trucks, trailers, and tractors that generally are used on the highway.</p><p>As background, a 12% federal excise tax is imposed on the sale price (of the first retail sale) of</p><ul><li>truck bodies and chassis suitable for use with a vehicle having a gross vehicle weight of over 33,000 pounds;</li><li>truck trailer and semitrailer bodies and chassis suitable for use with a vehicle having a gross vehicle weight over 26,000 pounds; and</li><li>tractors that are generally used for highway transportation in combination with a trailer or semitrailer, have a gross vehicle weight over 19,500 pounds, and have a gross combined\u00a0weight of greater than 33,000 pounds.</li></ul><p>Amounts collected from the excise tax on the retail sale of heavy trucks, trailers, and tractors are deposited into the Highway Trust Fund. (The Highway Trust Fund supports surface transportation programs and projects.)</p><p>Under current law, the excise tax on the retail sale of heavy trucks, trailers, and tractors expires on October 1, 2028.</p>"
        },
        "title": "Modern, Clean, and Safe Trucks Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2424.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong> Modern, Clean, and Safe Trucks Act of 2025</strong></p><p>This bill repeals the 12% federal excise tax imposed on the first retail sale of certain heavy trucks, trailers, and tractors that generally are used on the highway.</p><p>As background, a 12% federal excise tax is imposed on the sale price (of the first retail sale) of</p><ul><li>truck bodies and chassis suitable for use with a vehicle having a gross vehicle weight of over 33,000 pounds;</li><li>truck trailer and semitrailer bodies and chassis suitable for use with a vehicle having a gross vehicle weight over 26,000 pounds; and</li><li>tractors that are generally used for highway transportation in combination with a trailer or semitrailer, have a gross vehicle weight over 19,500 pounds, and have a gross combined\u00a0weight of greater than 33,000 pounds.</li></ul><p>Amounts collected from the excise tax on the retail sale of heavy trucks, trailers, and tractors are deposited into the Highway Trust Fund. (The Highway Trust Fund supports surface transportation programs and projects.)</p><p>Under current law, the excise tax on the retail sale of heavy trucks, trailers, and tractors expires on October 1, 2028.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr2424"
    },
    "title": "Modern, Clean, and Safe Trucks Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong> Modern, Clean, and Safe Trucks Act of 2025</strong></p><p>This bill repeals the 12% federal excise tax imposed on the first retail sale of certain heavy trucks, trailers, and tractors that generally are used on the highway.</p><p>As background, a 12% federal excise tax is imposed on the sale price (of the first retail sale) of</p><ul><li>truck bodies and chassis suitable for use with a vehicle having a gross vehicle weight of over 33,000 pounds;</li><li>truck trailer and semitrailer bodies and chassis suitable for use with a vehicle having a gross vehicle weight over 26,000 pounds; and</li><li>tractors that are generally used for highway transportation in combination with a trailer or semitrailer, have a gross vehicle weight over 19,500 pounds, and have a gross combined\u00a0weight of greater than 33,000 pounds.</li></ul><p>Amounts collected from the excise tax on the retail sale of heavy trucks, trailers, and tractors are deposited into the Highway Trust Fund. (The Highway Trust Fund supports surface transportation programs and projects.)</p><p>Under current law, the excise tax on the retail sale of heavy trucks, trailers, and tractors expires on October 1, 2028.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr2424"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2424ih.xml"
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
      "title": "Modern, Clean, and Safe Trucks Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modern, Clean, and Safe Trucks Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to repeal the excise tax on heavy trucks and trailers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T05:48:28Z"
    }
  ]
}
```
