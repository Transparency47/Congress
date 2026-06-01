# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1803?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1803
- Title: Fair Access to Co-ops for Veterans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1803
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-03-11T19:42:02Z
- Update date including text: 2026-03-11T19:42:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-11 - Committee: Subcommittee Hearings Held
- 2026-02-24 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-24 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-11 - Committee: Subcommittee Hearings Held
- 2026-02-24 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-24 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1803",
    "number": "1803",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Fair Access to Co-ops for Veterans Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-11T19:42:02Z",
    "updateDateIncludingText": "2026-03-11T19:42:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
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
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-24",
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
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-11",
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
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-03",
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
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-24T14:18:14Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-24T14:03:35Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-11T19:18:58Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-10T19:13:52Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "TN"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1803ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1803\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Ms. Meng (for herself and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for the improvement of the Department of Veterans Affairs loan guarantee for purchase of residential cooperative housing units, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Access to Co-ops for Veterans Act of 2025 .\n#### 2. Improvement of Department of Veterans Affairs loan guarantee for purchase of residential cooperative housing units\n##### (a) In general\nSection 3710 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(12), by striking With respect to a loan guaranteed after the date of the enactment of this paragraph and before the date that is five years after that date, to and inserting To ; and\n**(2)**\nby striking subsection (h) and inserting the following new subsection (h):\n(h) A loan may not be guaranteed under subsection (a)(12) before the date on which the Secretary prescribes regulations setting forth requirements for underwriting, loan processing, project standards, share eligibility, valuation, and other criteria the Secretary determines necessary. The Secretary shall ensure that such regulations are consistent, to the extent the Secretary determines suitable, with the requirements of the Federal National Mortgage Association for the purchase or securitization of cooperative housing loans. .\n##### (b) Loan fees\nSection 3729(b) of such title is amended\u2014\n**(1)**\nin paragraph (1), by striking The amount and inserting Except as provided in paragraph (5), the amount ; and\n**(2)**\nby adding at the end the following new paragraph:\n(5) In the case of an loan guaranteed under section 3710(a)(12) of this title, the amount of the fee shall be\u2014 (A) the amount determined from the loan fee table under paragraph (2), plus (B) 3.25 percent of the total amount of the loan guaranteed, insured, or made, or, in the case of a loan assumption, the unpaid principal balance of the loan on the date of the transfer of the property. .\n##### (c) Amount of loan\nSection 3703(a)(1)(A)(i)(IV) of such title is amended by striking or (8) and inserting (8), or (12) .\n##### (d) Treatment as residential property\nSuch title is further amended\u2014\n**(1)**\nin section 3704(c), by adding at the end the following new paragraph:\n(3) For purposes of this subsection, stock or membership in a cooperative housing corporation (as defined in section 216(b) of the Internal Revenue Code of 1986) for the purpose of entitling a person to occupy for dwelling purposes a single family residential unit in a development, project, or structure owned or leased by such corporation shall be treated as residential property. ; and\n**(2)**\nin section 3714, by adding at the end the following new subsection:\n(i) For purposes of this section, stock or membership in a cooperative housing corporation (as defined in section 216(b) of the Internal Revenue Code of 1986) for the purpose of entitling a person to occupy for dwelling purposes a single family residential unit in a development, project, or structure owned or leased by such corporation shall be treated as residential property. .\n##### (e) Authority To advertise\nThe Secretary of Veterans Affairs shall use the authority of the Secretary under section 532 of title 38, United States Code, to advertise the availability of loan guarantees for housing cooperative share loans under section 3710(a)(12) of such title and shall take such other appropriate actions as may be necessary, including by the issuance of guidance, to notify eligible veterans, participating lenders, and interested realtors of the availability of such loan guarantees and the procedures and requirements that apply to the obtaining of such guarantees.\n##### (f) Guidance\nNotwithstanding section 501 of such title, the Secretary of Veterans Affairs may issue guidance to implement section 3710 of title 38, United States Code, as amended by subsection (a), before prescribing new regulations under such section.",
      "versionDate": "2025-03-03",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-04-01T15:28:49Z"
          },
          {
            "name": "Cooperative and condominium housing",
            "updateDate": "2025-04-01T15:28:25Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-04-01T15:28:55Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-04-01T15:28:36Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-04-01T15:29:01Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-04-01T15:28:43Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-04-01T15:28:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-26T15:09:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119hr1803",
          "measure-number": "1803",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2026-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1803v00",
            "update-date": "2026-03-11"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fair Access to Co-ops for Veterans Act of 2025</strong></p><p>This bill revives and makes permanent the authority of the Department of Veterans Affairs (VA) home loan guarantee program to guarantee loans for a veteran\u2019s purchase of stock or membership in a cooperative housing corporation (i.e., co-op) for the purpose of entitling the veteran to occupy a single family residential unit.</p><p>For purposes of the administration of such loans, the bill</p><ul><li>establishes a fee rate of the usual fee plus\u00a03.25% of the total amount of the loan,</li><li>treats such cooperative housing units as residential property for purposes of imposing restrictions and liabilities, and</li><li>guarantees up to 25% of the amount of the loan for loans exceeding $144,000.\u00a0</li></ul><p>Additionally, the bill requires the VA to advertise the availability of loan guarantees for cooperative housing unit loans, including by issuing guidance and notifying eligible veterans.</p>"
        },
        "title": "Fair Access to Co-ops for Veterans Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1803.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Access to Co-ops for Veterans Act of 2025</strong></p><p>This bill revives and makes permanent the authority of the Department of Veterans Affairs (VA) home loan guarantee program to guarantee loans for a veteran\u2019s purchase of stock or membership in a cooperative housing corporation (i.e., co-op) for the purpose of entitling the veteran to occupy a single family residential unit.</p><p>For purposes of the administration of such loans, the bill</p><ul><li>establishes a fee rate of the usual fee plus\u00a03.25% of the total amount of the loan,</li><li>treats such cooperative housing units as residential property for purposes of imposing restrictions and liabilities, and</li><li>guarantees up to 25% of the amount of the loan for loans exceeding $144,000.\u00a0</li></ul><p>Additionally, the bill requires the VA to advertise the availability of loan guarantees for cooperative housing unit loans, including by issuing guidance and notifying eligible veterans.</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr1803"
    },
    "title": "Fair Access to Co-ops for Veterans Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Access to Co-ops for Veterans Act of 2025</strong></p><p>This bill revives and makes permanent the authority of the Department of Veterans Affairs (VA) home loan guarantee program to guarantee loans for a veteran\u2019s purchase of stock or membership in a cooperative housing corporation (i.e., co-op) for the purpose of entitling the veteran to occupy a single family residential unit.</p><p>For purposes of the administration of such loans, the bill</p><ul><li>establishes a fee rate of the usual fee plus\u00a03.25% of the total amount of the loan,</li><li>treats such cooperative housing units as residential property for purposes of imposing restrictions and liabilities, and</li><li>guarantees up to 25% of the amount of the loan for loans exceeding $144,000.\u00a0</li></ul><p>Additionally, the bill requires the VA to advertise the availability of loan guarantees for cooperative housing unit loans, including by issuing guidance and notifying eligible veterans.</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr1803"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1803ih.xml"
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
      "title": "Fair Access to Co-ops for Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Access to Co-ops for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for the improvement of the Department of Veterans Affairs loan guarantee for purchase of residential cooperative housing units, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T02:48:23Z"
    }
  ]
}
```
