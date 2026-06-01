# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/527
- Title: Prescription Pricing for the People Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 527
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-04-09T14:13:31Z
- Update date including text: 2026-04-09T14:13:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 42.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 42.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/527",
    "number": "527",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Prescription Pricing for the People Act of 2025",
    "type": "S",
    "updateDate": "2026-04-09T14:13:31Z",
    "updateDateIncludingText": "2026-04-09T14:13:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 42.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
            "date": "2025-04-10T20:24:09Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-03T14:15:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-11T21:06:27Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "WA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "KS"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "VT"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "AL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "DE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NC"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "CT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "WV"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "HI"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "OK"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AR"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TN"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s527is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 527\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Grassley (for himself, Ms. Cantwell , Mr. Marshall , Mr. Welch , Mr. Tuberville , Mr. Coons , Mr. Tillis , Mr. Blumenthal , Mrs. Capito , Ms. Hirono , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Federal Trade Commission to study the role of intermediaries in the pharmaceutical supply chain and provide Congress with appropriate policy recommendations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prescription Pricing for the People Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on the Judiciary of the Senate; and\n**(B)**\nthe Committee on the Judiciary of the House of Representatives.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n#### 3. Study of pharmaceutical supply chain intermediaries and merger activity\n##### (a) Report\nNot later than 1 year after the date of enactment of this Act, the Commission shall submit to the appropriate committees of Congress a report that\u2014\n**(1)**\naddresses at minimum\u2014\n**(A)**\nwhether pharmacy benefit managers\u2014\n**(i)**\ncharge payers a higher price than the reimbursement rate at which the pharmacy benefit managers reimburse pharmacies owned by the pharmacy benefit manager and pharmacies not owned by the pharmacy benefit manager;\n**(ii)**\nsteer patients for competitive advantage to any pharmacy, including a retail, mail-order, or any other type of pharmacy, in which the pharmacy benefit managers have an ownership interest;\n**(iii)**\naudit or review proprietary data, including acquisition costs, patient information, or dispensing information, of pharmacies not owned by the pharmacy benefit manager and use such proprietary data to increase revenue or market share for competitive advantage; or\n**(iv)**\nuse formulary designs to increase the market share of higher cost prescription drugs or depress the market share of lower cost prescription drugs (each net of rebates and discounts);\n**(B)**\ntrends or observations on the state of competition in the healthcare supply chain, particularly with regard to intermediaries and their integration with other intermediaries, suppliers, or payers of prescription drug benefits;\n**(C)**\nhow companies and payers assess the benefits, costs, and risks of contracting with intermediaries, including pharmacy services administrative organizations, and whether more information about the roles of intermediaries should be available to consumers and payers;\n**(D)**\nwhether there are any specific legal or regulatory obstacles the Commission currently faces in enforcing the antitrust and consumer protection laws in the pharmaceutical supply chain, including the pharmacy benefit manager marketplace and pharmacy services administrative organizations; and\n**(E)**\nwhether there are any specific legal or regulatory obstacles that contribute to the cost of prescription drug prices; and\n**(2)**\nprovides\u2014\n**(A)**\nobservations or conclusions drawn from the November 2017 roundtable entitled Understanding Competition in Prescription Drug Markets: Entry and Supply Chain Dynamics and any similar efforts;\n**(B)**\nspecific actions the Commission intends to take as a result of the November 2017 roundtable, and any similar efforts, including a detailed description of relevant forthcoming actions, additional research or roundtable discussions, consumer education efforts, or enforcement actions; and\n**(C)**\npolicy or legislative recommendations to\u2014\n**(i)**\nimprove transparency and competition in the pharmaceutical supply chain;\n**(ii)**\nprevent and deter anticompetitive behavior in the pharmaceutical supply chain; and\n**(iii)**\nbest ensure that consumers benefit from any cost savings or efficiencies that may result from mergers and consolidations.\n##### (b) Interim report\nNot later than 180 days after the date of enactment of this Act, the Commission shall submit to the appropriate committees of Congress an interim report on the progress of the report required by subsection (a), along with preliminary findings and conclusions based on information collected to that date.\n#### 4. Report\nThe Commission shall submit to the appropriate committees of Congress a report that includes\u2014\n**(1)**\nthe number and nature of complaints received by the Commission relating to an allegation of anticompetitive conduct by a manufacturer of a sole-source drug;\n**(2)**\nthe ability of the Commission to bring an enforcement action against a manufacturer of a sole-source drug; and\n**(3)**\npolicy or legislative recommendations to strengthen enforcement actions relating to anticompetitive behavior.",
      "versionDate": "2025-02-11",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s527rs.xml",
      "text": "II\nCalendar No. 42\n119th CONGRESS\n1st Session\nS. 527\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Grassley (for himself, Ms. Cantwell , Mr. Marshall , Mr. Welch , Mr. Tuberville , Mr. Coons , Mr. Tillis , Mr. Blumenthal , Mrs. Capito , Ms. Hirono , Mr. Lankford , Mr. Boozman , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nApril 10, 2025 Reported by Mr. Grassley , without amendment\nA BILL\nTo require the Federal Trade Commission to study the role of intermediaries in the pharmaceutical supply chain and provide Congress with appropriate policy recommendations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prescription Pricing for the People Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on the Judiciary of the Senate; and\n**(B)**\nthe Committee on the Judiciary of the House of Representatives.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n#### 3. Study of pharmaceutical supply chain intermediaries and merger activity\n##### (a) Report\nNot later than 1 year after the date of enactment of this Act, the Commission shall submit to the appropriate committees of Congress a report that\u2014\n**(1)**\naddresses at minimum\u2014\n**(A)**\nwhether pharmacy benefit managers\u2014\n**(i)**\ncharge payers a higher price than the reimbursement rate at which the pharmacy benefit managers reimburse pharmacies owned by the pharmacy benefit manager and pharmacies not owned by the pharmacy benefit manager;\n**(ii)**\nsteer patients for competitive advantage to any pharmacy, including a retail, mail-order, or any other type of pharmacy, in which the pharmacy benefit managers have an ownership interest;\n**(iii)**\naudit or review proprietary data, including acquisition costs, patient information, or dispensing information, of pharmacies not owned by the pharmacy benefit manager and use such proprietary data to increase revenue or market share for competitive advantage; or\n**(iv)**\nuse formulary designs to increase the market share of higher cost prescription drugs or depress the market share of lower cost prescription drugs (each net of rebates and discounts);\n**(B)**\ntrends or observations on the state of competition in the healthcare supply chain, particularly with regard to intermediaries and their integration with other intermediaries, suppliers, or payers of prescription drug benefits;\n**(C)**\nhow companies and payers assess the benefits, costs, and risks of contracting with intermediaries, including pharmacy services administrative organizations, and whether more information about the roles of intermediaries should be available to consumers and payers;\n**(D)**\nwhether there are any specific legal or regulatory obstacles the Commission currently faces in enforcing the antitrust and consumer protection laws in the pharmaceutical supply chain, including the pharmacy benefit manager marketplace and pharmacy services administrative organizations; and\n**(E)**\nwhether there are any specific legal or regulatory obstacles that contribute to the cost of prescription drug prices; and\n**(2)**\nprovides\u2014\n**(A)**\nobservations or conclusions drawn from the November 2017 roundtable entitled Understanding Competition in Prescription Drug Markets: Entry and Supply Chain Dynamics and any similar efforts;\n**(B)**\nspecific actions the Commission intends to take as a result of the November 2017 roundtable, and any similar efforts, including a detailed description of relevant forthcoming actions, additional research or roundtable discussions, consumer education efforts, or enforcement actions; and\n**(C)**\npolicy or legislative recommendations to\u2014\n**(i)**\nimprove transparency and competition in the pharmaceutical supply chain;\n**(ii)**\nprevent and deter anticompetitive behavior in the pharmaceutical supply chain; and\n**(iii)**\nbest ensure that consumers benefit from any cost savings or efficiencies that may result from mergers and consolidations.\n##### (b) Interim report\nNot later than 180 days after the date of enactment of this Act, the Commission shall submit to the appropriate committees of Congress an interim report on the progress of the report required by subsection (a), along with preliminary findings and conclusions based on information collected to that date.\n#### 4. Report\nThe Commission shall submit to the appropriate committees of Congress a report that includes\u2014\n**(1)**\nthe number and nature of complaints received by the Commission relating to an allegation of anticompetitive conduct by a manufacturer of a sole-source drug;\n**(2)**\nthe ability of the Commission to bring an enforcement action against a manufacturer of a sole-source drug; and\n**(3)**\npolicy or legislative recommendations to strengthen enforcement actions relating to anticompetitive behavior.",
      "versionDate": "2025-04-10",
      "versionType": "Reported in Senate"
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
            "name": "Business ethics",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Business records",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Competition and antitrust",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-05-22T14:09:58Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-09T14:13:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-15T13:25:45Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s527is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s527rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Prescription Pricing for the People Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T11:03:21Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Prescription Pricing for the People Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prescription Pricing for the People Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Federal Trade Commission to study the role of intermediaries in the pharmaceutical supply chain and provide Congress with appropriate policy recommendations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:33Z"
    }
  ]
}
```
