# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8043?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8043
- Title: Vets CLEAR Act
- Congress: 119
- Bill type: HR
- Bill number: 8043
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-04-17T08:07:18Z
- Update date including text: 2026-04-17T08:07:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-25 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-25 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8043",
    "number": "8043",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001133",
        "district": "6",
        "firstName": "Juan",
        "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
        "lastName": "Ciscomani",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Vets CLEAR Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:18Z",
    "updateDateIncludingText": "2026-04-17T08:07:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
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
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
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
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:02:30Z",
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
                "date": "2026-04-15T13:31:19Z",
                "name": "Reported by"
              },
              {
                "date": "2026-04-15T13:07:45Z",
                "name": "Markup by"
              },
              {
                "date": "2026-03-25T13:07:13Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
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
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8043ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8043\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Mr. Ciscomani (for himself and Ms. Bynum ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the efficiency of the recovery and collection of revenue for the Department of Veterans Affairs Medical Care Collections Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Vets Collections, Liquidity, and Efficiency Accountability for Reinvestment Act or the Vets CLEAR Act .\n#### 2. Provide flexibility and efficiency for collection of revenue for Department of Veterans Affairs Medical Care Collections Fund\n##### (a) In general\nSection 1729A of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by adding at the end the following new paragraphs:\n(11) Sections 3711 and 3729 through 3733 of title 31, to the extent that such recovery or collection is based on medical care, services, or medication provided or paid for under this chapter. (12) Amounts recovered or collected through administrative, legal, or judicial processes, including investigations and audits, to the extent that such recovery or collection is based on medical care, services, or medication provided or paid for under this chapter. ;\n**(2)**\nby redesignating subsections (c), (d), and (e) as subsections (d), (e), and (f), respectively; and\n**(3)**\nby inserting after subsection (b) the following new subsection:\n(c) (1) Notwithstanding any other provision of law, funds directed to the Medical Services account to reimburse such account for the costs of care provided under the following authorities may, at the discretion of the Secretary, be deposited in the Medical Care Collections Fund: (A) Section 1781 of this title. (B) Section 8111 of this title. (2) The authority of the Secretary to deposit amounts into the Medical Care Collections Fund pursuant to this subsection shall expire on September 30, 2028. .\n##### (b) GAO reports\nSuch section is further amended by adding at the end the following new subsection:\n(g) (1) Not later than 180 days after the date of enactment of this subsection, and not less frequently than once every 180 days thereafter during period the authority under subsection (c) is effective, the Comptroller General of the United States shall submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a report on amounts deposited into the Medical Care Collections Fund under this section. (2) Each report required under paragraph (1) shall include\u2014 (A) the total amount of funds recovered or collected during the period covered by the report, disaggregated by source of recovery or collection; and (B) a description of how such funds were expended by the Department, including the categories of medical care, services, staffing, or other purposes for which the funds were used. .",
      "versionDate": "2026-03-24",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-09T16:44:39Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8043ih.xml"
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
      "title": "Vets CLEAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Vets CLEAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Vets Collections, Liquidity, and Efficiency Accountability for Reinvestment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the efficiency of the recovery and collection of revenue for the Department of Veterans Affairs Medical Care Collections Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:33Z"
    }
  ]
}
```
