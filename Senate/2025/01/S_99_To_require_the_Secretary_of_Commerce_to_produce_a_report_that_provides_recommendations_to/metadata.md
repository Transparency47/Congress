# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/99?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/99
- Title: Strengthening Support for American Manufacturing Act
- Congress: 119
- Bill type: S
- Bill number: 99
- Origin chamber: Senate
- Introduced date: 2025-01-15
- Update date: 2026-04-09T14:16:23Z
- Update date including text: 2026-04-09T14:16:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in Senate
- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-03-31 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-9.
- 2025-03-31 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-9.
- 2025-03-31 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 35.
- 2025-10-23 - Floor: Message on Senate action sent to the House.
- 2025-10-23 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S7734; text: CR S7734-7735)
- 2025-10-23 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-10-24 14:02:44 - Floor: Received in the House.
- 2025-10-24 14:15:23 - Floor: Held at the desk.
- Latest action: 2025-01-15: Introduced in Senate

## Actions

- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-03-31 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-9.
- 2025-03-31 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-9.
- 2025-03-31 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 35.
- 2025-10-23 - Floor: Message on Senate action sent to the House.
- 2025-10-23 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S7734; text: CR S7734-7735)
- 2025-10-23 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-10-24 14:02:44 - Floor: Received in the House.
- 2025-10-24 14:15:23 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/99",
    "number": "99",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Strengthening Support for American Manufacturing Act",
    "type": "S",
    "updateDate": "2026-04-09T14:16:23Z",
    "updateDateIncludingText": "2026-04-09T14:16:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-10-24",
      "actionTime": "14:15:23",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-10-24",
      "actionTime": "14:02:44",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S7734; text: CR S7734-7735)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 35.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-9.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-9.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-15",
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
        "item": [
          {
            "date": "2025-03-31T21:44:38Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T15:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-15T19:24:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s99is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 99\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2025 Mr. Peters (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Commerce to produce a report that provides recommendations to improve the effectiveness, efficiency, and impact of Department of Commerce programs related to supply chain resilience and manufacturing and industrial innovation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Support for American Manufacturing Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(2) Covered offices and bureaus**\nThe term covered offices and bureaus means offices and bureaus of the Department of Commerce identified under section 3(a)(1).\n**(3) Critical supply chain**\nThe term critical supply chain means an end-to-end system that converts raw materials into finished products in critical sectors, including in\u2014\n**(A)**\nthe defense industrial base;\n**(B)**\nthe public health and biological preparedness industrial base;\n**(C)**\nthe information and communications technology industrial base;\n**(D)**\nthe energy sector industrial base;\n**(E)**\nthe transportation industrial base; and\n**(F)**\nagricultural supply chains.\n**(4) Critical supply chain resilience**\nThe term critical supply chain resilience means mitigating gaps and vulnerabilities in critical supply chains, including by\u2014\n**(A)**\nreducing risk of malicious sabotage or external or internal manipulation; and\n**(B)**\nimproving the ability to withstand supply chain interruptions such as logistical challenges and workforce, materials, equipment, or product shortages.\n**(5) Manufacturing and industrial innovation**\nThe term manufacturing and industrial innovation means\u2014\n**(A)**\nproviding assistance, resources, or services to manufacturers or manufacturing workers in the United States;\n**(B)**\noffering expertise, improvements, research, and development or other assistance in technological innovations or advanced manufacturing in partnership with or for use by manufacturers in the United States; or\n**(C)**\ndeveloping policy that substantially impacts the manufacturing sector in the United States.\n**(6) Secretary**\nThe term Secretary means the Secretary of Commerce.\n#### 3. Study relating to manufacturing programs of the Department of Commerce\n##### (a) Assessment\nNot later than 1 year after the date of enactment of this Act, the Secretary shall produce a report that\u2014\n**(1)**\nidentifies offices and bureaus of the Department of Commerce with responsibilities related to\u2014\n**(A)**\ncritical supply chain resilience; and\n**(B)**\nmanufacturing and industrial innovation;\n**(2)**\nidentifies the duties, responsibilities, programs, and expertise relevant to critical supply chain resilience and manufacturing and industrial innovation of each covered office and bureau;\n**(3)**\nidentifies and assesses the purpose, statutory authority, effectiveness, efficiency, and limitations of each covered office and bureau;\n**(4)**\nidentifies gaps between offices with duplicative duties, responsibilities, programs, and expertise within the Department of Commerce that are implementing activities related to critical supply chain resilience and manufacturing and industrial innovation; and\n**(5)**\nprovides recommendations to improve the effectiveness, efficiency, and impact of each covered office and bureau, including recommendations to\u2014\n**(A)**\noptimize operations within or across covered offices and bureaus;\n**(B)**\nimprove coordination across covered offices and bureaus; and\n**(C)**\nimprove coordination with Federal agencies implementing similar activities related to critical supply chain resilience and manufacturing and industrial innovation.\n##### (b) National Academy of Public Administration\nThe Secretary shall contract with the National Academy of Public Administration in producing the report under subsection (a).\n##### (c) Report\nNot later than 180 days after the date on which the Secretary produces the report under subsection (a), the Secretary shall submit to the appropriate committees of Congress\u2014\n**(1)**\nthe report produced under subsection (a);\n**(2)**\nrecommendations for potential legislative action addressing recommendations in the report produced under subsection (a); and\n**(3)**\na response from the Secretary to the recommendations included in the report produced under subsection (a).",
      "versionDate": "2025-01-15",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s99rs.xml",
      "text": "II\nCalendar No. 35\n119th CONGRESS\n1st Session\nS. 99\n[Report No. 119\u20139]\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2025 Mr. Peters (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nMarch 31, 2025 Reported by Mr. Cruz , without amendment\nA BILL\nTo require the Secretary of Commerce to produce a report that provides recommendations to improve the effectiveness, efficiency, and impact of Department of Commerce programs related to supply chain resilience and manufacturing and industrial innovation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Support for American Manufacturing Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(2) Covered offices and bureaus**\nThe term covered offices and bureaus means offices and bureaus of the Department of Commerce identified under section 3(a)(1).\n**(3) Critical supply chain**\nThe term critical supply chain means an end-to-end system that converts raw materials into finished products in critical sectors, including in\u2014\n**(A)**\nthe defense industrial base;\n**(B)**\nthe public health and biological preparedness industrial base;\n**(C)**\nthe information and communications technology industrial base;\n**(D)**\nthe energy sector industrial base;\n**(E)**\nthe transportation industrial base; and\n**(F)**\nagricultural supply chains.\n**(4) Critical supply chain resilience**\nThe term critical supply chain resilience means mitigating gaps and vulnerabilities in critical supply chains, including by\u2014\n**(A)**\nreducing risk of malicious sabotage or external or internal manipulation; and\n**(B)**\nimproving the ability to withstand supply chain interruptions such as logistical challenges and workforce, materials, equipment, or product shortages.\n**(5) Manufacturing and industrial innovation**\nThe term manufacturing and industrial innovation means\u2014\n**(A)**\nproviding assistance, resources, or services to manufacturers or manufacturing workers in the United States;\n**(B)**\noffering expertise, improvements, research, and development or other assistance in technological innovations or advanced manufacturing in partnership with or for use by manufacturers in the United States; or\n**(C)**\ndeveloping policy that substantially impacts the manufacturing sector in the United States.\n**(6) Secretary**\nThe term Secretary means the Secretary of Commerce.\n#### 3. Study relating to manufacturing programs of the Department of Commerce\n##### (a) Assessment\nNot later than 1 year after the date of enactment of this Act, the Secretary shall produce a report that\u2014\n**(1)**\nidentifies offices and bureaus of the Department of Commerce with responsibilities related to\u2014\n**(A)**\ncritical supply chain resilience; and\n**(B)**\nmanufacturing and industrial innovation;\n**(2)**\nidentifies the duties, responsibilities, programs, and expertise relevant to critical supply chain resilience and manufacturing and industrial innovation of each covered office and bureau;\n**(3)**\nidentifies and assesses the purpose, statutory authority, effectiveness, efficiency, and limitations of each covered office and bureau;\n**(4)**\nidentifies gaps between offices with duplicative duties, responsibilities, programs, and expertise within the Department of Commerce that are implementing activities related to critical supply chain resilience and manufacturing and industrial innovation; and\n**(5)**\nprovides recommendations to improve the effectiveness, efficiency, and impact of each covered office and bureau, including recommendations to\u2014\n**(A)**\noptimize operations within or across covered offices and bureaus;\n**(B)**\nimprove coordination across covered offices and bureaus; and\n**(C)**\nimprove coordination with Federal agencies implementing similar activities related to critical supply chain resilience and manufacturing and industrial innovation.\n##### (b) National Academy of Public Administration\nThe Secretary shall contract with the National Academy of Public Administration in producing the report under subsection (a).\n##### (c) Report\nNot later than 180 days after the date on which the Secretary produces the report under subsection (a), the Secretary shall submit to the appropriate committees of Congress\u2014\n**(1)**\nthe report produced under subsection (a);\n**(2)**\nrecommendations for potential legislative action addressing recommendations in the report produced under subsection (a); and\n**(3)**\na response from the Secretary to the recommendations included in the report produced under subsection (a).",
      "versionDate": "2025-03-31",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s99es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 99\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo require the Secretary of Commerce to produce a report that provides recommendations to improve the effectiveness, efficiency, and impact of Department of Commerce programs related to supply chain resilience and manufacturing and industrial innovation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Support for American Manufacturing Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(2) Covered offices and bureaus**\nThe term covered offices and bureaus means offices and bureaus of the Department of Commerce identified under section 3(a)(1).\n**(3) Critical supply chain**\nThe term critical supply chain means an end-to-end system that converts raw materials into finished products in critical sectors, including in\u2014\n**(A)**\nthe defense industrial base;\n**(B)**\nthe public health and biological preparedness industrial base;\n**(C)**\nthe information and communications technology industrial base;\n**(D)**\nthe energy sector industrial base;\n**(E)**\nthe transportation industrial base; and\n**(F)**\nagricultural supply chains.\n**(4) Critical supply chain resilience**\nThe term critical supply chain resilience means mitigating gaps and vulnerabilities in critical supply chains, including by\u2014\n**(A)**\nreducing risk of malicious sabotage or external or internal manipulation; and\n**(B)**\nimproving the ability to withstand supply chain interruptions such as logistical challenges and workforce, materials, equipment, or product shortages.\n**(5) Manufacturing and industrial innovation**\nThe term manufacturing and industrial innovation means\u2014\n**(A)**\nproviding assistance, resources, or services to manufacturers or manufacturing workers in the United States;\n**(B)**\noffering expertise, improvements, research, and development or other assistance in technological innovations or advanced manufacturing in partnership with or for use by manufacturers in the United States; or\n**(C)**\ndeveloping policy that substantially impacts the manufacturing sector in the United States.\n**(6) Secretary**\nThe term Secretary means the Secretary of Commerce.\n#### 3. Study relating to manufacturing programs of the Department of Commerce\n##### (a) Assessment\nNot later than 1 year after the date of enactment of this Act, the Secretary shall produce a report that\u2014\n**(1)**\nidentifies offices and bureaus of the Department of Commerce with responsibilities related to\u2014\n**(A)**\ncritical supply chain resilience; and\n**(B)**\nmanufacturing and industrial innovation;\n**(2)**\nidentifies the duties, responsibilities, programs, and expertise relevant to critical supply chain resilience and manufacturing and industrial innovation of each covered office and bureau;\n**(3)**\nidentifies and assesses the purpose, statutory authority, effectiveness, efficiency, and limitations of each covered office and bureau;\n**(4)**\nidentifies gaps between offices with duplicative duties, responsibilities, programs, and expertise within the Department of Commerce that are implementing activities related to critical supply chain resilience and manufacturing and industrial innovation; and\n**(5)**\nprovides recommendations to improve the effectiveness, efficiency, and impact of each covered office and bureau, including recommendations to\u2014\n**(A)**\noptimize operations within or across covered offices and bureaus;\n**(B)**\nimprove coordination across covered offices and bureaus; and\n**(C)**\nimprove coordination with Federal agencies implementing similar activities related to critical supply chain resilience and manufacturing and industrial innovation.\n##### (b) National Academy of Public Administration\nThe Secretary shall contract with the National Academy of Public Administration in producing the report under subsection (a).\n##### (c) Report\nNot later than 180 days after the date on which the Secretary produces the report under subsection (a), the Secretary shall submit to the appropriate committees of Congress\u2014\n**(1)**\nthe report produced under subsection (a);\n**(2)**\nrecommendations for potential legislative action addressing recommendations in the report produced under subsection (a); and\n**(3)**\na response from the Secretary to the recommendations included in the report produced under subsection (a).",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-02-13T16:36:35Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2025-02-13T16:36:35Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-13T16:36:35Z"
          },
          {
            "name": "Industrial policy and productivity",
            "updateDate": "2025-02-13T16:36:35Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-02-13T16:36:35Z"
          },
          {
            "name": "Product development and innovation",
            "updateDate": "2025-02-13T16:36:35Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-09T14:16:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-05T16:24:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
    "originChamber": "Senate",
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
          "measure-id": "id119s99",
          "measure-number": "99",
          "measure-type": "s",
          "orig-publish-date": "2025-01-15",
          "originChamber": "SENATE",
          "update-date": "2025-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s99v00",
            "update-date": "2025-05-12"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Strengthening Support for American Manufacturing Act</strong></p><p>This bill requires the Department of Commerce to contract with the National Academy of Public Administration to study and report on the offices and bureaus of the department that are relevant to critical supply chain resilience and manufacturing and industrial innovation.</p><p>The report must evaluate the purpose, statutory authority, effectiveness, efficiency, and limitations of each such office and bureau and provide recommendations to improve their effectiveness, efficiency, and impact.</p>"
        },
        "title": "Strengthening Support for American Manufacturing Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s99.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Strengthening Support for American Manufacturing Act</strong></p><p>This bill requires the Department of Commerce to contract with the National Academy of Public Administration to study and report on the offices and bureaus of the department that are relevant to critical supply chain resilience and manufacturing and industrial innovation.</p><p>The report must evaluate the purpose, statutory authority, effectiveness, efficiency, and limitations of each such office and bureau and provide recommendations to improve their effectiveness, efficiency, and impact.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119s99"
    },
    "title": "Strengthening Support for American Manufacturing Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Strengthening Support for American Manufacturing Act</strong></p><p>This bill requires the Department of Commerce to contract with the National Academy of Public Administration to study and report on the offices and bureaus of the department that are relevant to critical supply chain resilience and manufacturing and industrial innovation.</p><p>The report must evaluate the purpose, statutory authority, effectiveness, efficiency, and limitations of each such office and bureau and provide recommendations to improve their effectiveness, efficiency, and impact.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119s99"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s99is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s99rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s99es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Strengthening Support for American Manufacturing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-24T11:03:14Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Strengthening Support for American Manufacturing Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-10-24T02:08:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Strengthening Support for American Manufacturing Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-03T13:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Support for American Manufacturing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Commerce to produce a report that provides recommendations to improve the effectiveness, efficiency, and impact of Department of Commerce programs related to supply chain resilience and manufacturing and industrial innovation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T15:18:22Z"
    }
  ]
}
```
