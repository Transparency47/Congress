# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7266?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7266
- Title: Rural and Municipal Utility Cybersecurity Act
- Congress: 119
- Bill type: HR
- Bill number: 7266
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-05-27T18:41:27Z
- Update date including text: 2026-05-27T18:41:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-27 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-04-30 - Calendars: Placed on the Union Calendar, Calendar No. 545.
- 2026-04-30 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-629.
- 2026-04-30 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-629.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-27 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-04-30 - Calendars: Placed on the Union Calendar, Calendar No. 545.
- 2026-04-30 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-629.
- 2026-04-30 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-629.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7266",
    "number": "7266",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Rural and Municipal Utility Cybersecurity Act",
    "type": "HR",
    "updateDate": "2026-05-27T18:41:27Z",
    "updateDateIncludingText": "2026-05-27T18:41:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-04-30",
      "calendarNumber": {
        "calendar": "U00545"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 545.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-629.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-629.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
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
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
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
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
        "item": [
          {
            "date": "2026-04-30T19:08:06Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-27T17:32:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-04T22:38:49Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-04T22:37:54Z",
                "name": "Markup by"
              },
              {
                "date": "2026-01-27T22:37:02Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "VA"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7266ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7266\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mrs. Miller-Meeks (for herself and Ms. McClellan ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to reauthorize the Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural and Municipal Utility Cybersecurity Act .\n#### 2. Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program\nSection 40124 of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18723 ) is amended to read as follows:\n40124. Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program (a) Definitions In this section: (1) Advanced cybersecurity technology The term advanced cybersecurity technology means any technology, operational capability, or service, including computer hardware, software, or a related asset, that enhances the security posture of electric utilities through improvements in the ability to protect against, detect, respond to, or recover from a cybersecurity threat. (2) Bulk-power system The term bulk-power system has the meaning given the term in section 215(a) of the Federal Power Act. (3) Cybersecurity threat The term cybersecurity threat has the meaning given the term in section 2200 of the Homeland Security Act of 2002. (4) Defense critical electric infrastructure The term defense critical electric infrastructure has the meaning given the term in section 215A(a) of the Federal Power Act. (5) Eligible entity The term eligible entity means\u2014 (A) a rural electric cooperative; (B) an electric utility owned by a political subdivision of a State, such as a municipally owned electric utility; (C) an electric utility owned by any agency, authority, corporation, or instrumentality of 1 or more political subdivisions of a State; (D) a not-for-profit entity that is in a partnership with not fewer than 6 entities described in subparagraph (A), (B), or (C); and (E) an investor-owned electric utility that sells less than 4,000,000 megawatt hours of electricity per year. (6) Program The term Program means the Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program established under subsection (b). (b) Establishment The Secretary shall maintain a program, to be known as the Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program, to provide technical assistance and award funding, including grants, cooperative agreements, and prizes, to eligible entities to protect against, detect, respond to, and recover from cybersecurity threats. (c) Objectives The objectives of the Program shall be\u2014 (1) to deploy advanced cybersecurity technologies for electric utility systems; and (2) to increase the participation of eligible entities in cybersecurity threat information sharing programs. (d) Awards (1) In general In carrying out the Program, the Secretary\u2014 (A) shall, subject to the availability of appropriations, provide technical assistance, and award funding, including grants, cooperative agreements, and prizes, to eligible entities on a competitive or noncompetitive basis; (B) shall develop criteria for providing such technical assistance and awarding such funding; (C) may enter into agreements that can facilitate the objectives described in subsection (c) with eligible entities to provide technical assistance or award funding, including grants, cooperative agreements, and prizes; and (D) shall establish a process to ensure, to the extent practicable, that all eligible entities are informed about opportunities to receive technical assistance or funding, including grants, cooperative agreements, and prizes. (2) Priority for funding and technical assistance In providing technical assistance and awarding funding, including grants, cooperative agreements, and prizes, under the Program, the Secretary shall give priority to an eligible entity that, as determined by the Secretary\u2014 (A) has limited cybersecurity resources; (B) owns assets critical to the reliability of the bulk-power system; or (C) owns or operates defense critical electric infrastructure. (e) Protection of information Information shared by or with the Federal Government or a State, Tribal, or local government under the Program shall be deemed voluntarily shared information and exempt from disclosure under section 552 of title 5, United States Code (commonly known as the Freedom of Information Act), or any provision of any State, Tribal, or local freedom of information law, open government law, open meetings law, open records law, sunshine law, or similar law requiring the disclosure of information or records. (f) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $250,000,000 for the period of fiscal years 2026 through 2030. .",
      "versionDate": "2026-01-27",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7266rh.xml",
      "text": "IB\nUnion Calendar No. 545\n119th CONGRESS\n2d Session\nH. R. 7266\n[Report No. 119\u2013629]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mrs. Miller-Meeks (for herself and Ms. McClellan ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nApril 30, 2026 Additional sponsor: Mrs. Harshbarger\nApril 30, 2026 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to reauthorize the Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural and Municipal Utility Cybersecurity Act .\n#### 2. Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program\nSection 40124 of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18723 ) is amended to read as follows:\n40124. Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program (a) Definitions In this section: (1) Advanced cybersecurity technology The term advanced cybersecurity technology means any technology, operational capability, or service, including computer hardware, software, or a related asset, that enhances the security posture of electric utilities through improvements in the ability to protect against, detect, respond to, or recover from a cybersecurity threat. (2) Bulk-power system The term bulk-power system has the meaning given the term in section 215(a) of the Federal Power Act. (3) Cybersecurity threat The term cybersecurity threat has the meaning given the term in section 2200 of the Homeland Security Act of 2002. (4) Defense critical electric infrastructure The term defense critical electric infrastructure has the meaning given the term in section 215A(a) of the Federal Power Act. (5) Eligible entity The term eligible entity means\u2014 (A) a rural electric cooperative; (B) an electric utility owned by a political subdivision of a State, such as a municipally owned electric utility; (C) an electric utility owned by any agency, authority, corporation, or instrumentality of 1 or more political subdivisions of a State; (D) a not-for-profit entity that is in a partnership with not fewer than 6 entities described in subparagraph (A), (B), or (C); and (E) an investor-owned electric utility that sells less than 4,000,000 megawatt hours of electricity per year. (6) Program The term Program means the Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program established under subsection (b). (b) Establishment The Secretary shall maintain a program, to be known as the Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program, to provide technical assistance and award funding, including grants, cooperative agreements, and prizes, to eligible entities to protect against, detect, respond to, and recover from cybersecurity threats. (c) Objectives The objectives of the Program shall be\u2014 (1) to deploy advanced cybersecurity technologies for electric utility systems; and (2) to increase the participation of eligible entities in cybersecurity threat information sharing programs. (d) Awards (1) In general In carrying out the Program, the Secretary\u2014 (A) shall, subject to the availability of appropriations, provide technical assistance, and award funding, including grants, cooperative agreements, and prizes, to eligible entities on a competitive or noncompetitive basis; (B) shall develop criteria for providing such technical assistance and awarding such funding; (C) may enter into agreements that can facilitate the objectives described in subsection (c) with eligible entities to provide technical assistance or award funding, including grants, cooperative agreements, and prizes; and (D) shall establish a process to ensure, to the extent practicable, that all eligible entities are informed about opportunities to receive technical assistance or funding, including grants, cooperative agreements, and prizes. (2) Priority for funding and technical assistance In providing technical assistance and awarding funding, including grants, cooperative agreements, and prizes, under the Program, the Secretary shall give priority to an eligible entity that, as determined by the Secretary\u2014 (A) has limited cybersecurity resources; (B) owns assets critical to the reliability of the bulk-power system; or (C) owns or operates defense critical electric infrastructure. (e) Protection of information Information shared by or with the Federal Government or a State, Tribal, or local government under the Program shall be deemed voluntarily shared information and exempt from disclosure under section 552 of title 5, United States Code (commonly known as the Freedom of Information Act), or any provision of any State, Tribal, or local freedom of information law, open government law, open meetings law, open records law, sunshine law, or similar law requiring the disclosure of information or records. (f) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $250,000,000 for the period of fiscal years 2026 through 2030. .",
      "versionDate": "2026-04-30",
      "versionType": "Reported in House"
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
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-10T17:42:57Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-02-10T17:43:14Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-02-10T17:44:15Z"
          },
          {
            "name": "Infrastructure development",
            "updateDate": "2026-02-10T17:43:29Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2026-02-10T17:42:50Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-10T17:43:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-05-04T12:27:08Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7266ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7266rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Rural and Municipal Utility Cybersecurity Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-01T08:53:25Z"
    },
    {
      "title": "Rural and Municipal Utility Cybersecurity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural and Municipal Utility Cybersecurity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Infrastructure Investment and Jobs Act to reauthorize the Rural and Municipal Utility Advanced Cybersecurity Grant and Technical Assistance Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:18:18Z"
    }
  ]
}
```
