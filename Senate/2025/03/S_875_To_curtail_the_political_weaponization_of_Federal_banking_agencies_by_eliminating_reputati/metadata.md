# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/875?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/875
- Title: FIRM Act
- Congress: 119
- Bill type: S
- Bill number: 875
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-03-12T15:09:35Z
- Update date including text: 2026-03-12T15:09:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-03-13 - Committee: Committee on Banking, Housing, and Urban Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-03-18 - Committee: Committee on Banking, Housing, and Urban Affairs. Reported by Senator Scott SC, under authority of the order of the Senate of 03/14/2025 with an amendment in the nature of a substitute. Without written report.
- 2025-03-18 - Committee: Committee on Banking, Housing, and Urban Affairs. Reported by Senator Scott SC, under authority of the order of the Senate of 03/14/2025 with an amendment in the nature of a substitute. Without written report.
- 2025-03-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 32.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-03-13 - Committee: Committee on Banking, Housing, and Urban Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-03-18 - Committee: Committee on Banking, Housing, and Urban Affairs. Reported by Senator Scott SC, under authority of the order of the Senate of 03/14/2025 with an amendment in the nature of a substitute. Without written report.
- 2025-03-18 - Committee: Committee on Banking, Housing, and Urban Affairs. Reported by Senator Scott SC, under authority of the order of the Senate of 03/14/2025 with an amendment in the nature of a substitute. Without written report.
- 2025-03-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 32.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/875",
    "number": "875",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "FIRM Act",
    "type": "S",
    "updateDate": "2026-03-12T15:09:35Z",
    "updateDateIncludingText": "2026-03-12T15:09:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 32.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Banking, Housing, and Urban Affairs. Reported by Senator Scott SC, under authority of the order of the Senate of 03/14/2025 with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Banking, Housing, and Urban Affairs. Reported by Senator Scott SC, under authority of the order of the Senate of 03/14/2025 with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Banking, Housing, and Urban Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": [
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2025-10-09",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2025-10-09",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "2"
          },
          "amendedBill": {
            "congress": "119",
            "number": "875",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "FIRM Act",
            "type": "S",
            "updateDateIncludingText": "2026-03-12"
          },
          "chamber": "Senate",
          "congress": "119",
          "cosponsors": {
            "count": "1",
            "countIncludingWithdrawnCosponsors": "1",
            "item": {
              "bioguideId": "W000817",
              "firstName": "Elizabeth",
              "fullName": "Sen. Warren, Elizabeth [D-MA]",
              "isOriginalCosponsor": "True",
              "lastName": "Warren",
              "middleName": "A.",
              "party": "D",
              "sponsorshipDate": "2025-10-09",
              "state": "MA"
            }
          },
          "number": "3931",
          "sponsors": {
            "item": {
              "bioguideId": "R000122",
              "firstName": "John",
              "fullName": "Sen. Reed, Jack [D-RI]",
              "lastName": "Reed",
              "middleName": "F.",
              "party": "D",
              "state": "RI"
            }
          },
          "submittedDate": "2025-10-09T04:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2025-10-09T18:10:16Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2025-10-09",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2025-10-09",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "2"
          },
          "amendedBill": {
            "congress": "119",
            "number": "875",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "FIRM Act",
            "type": "S",
            "updateDateIncludingText": "2026-03-12"
          },
          "chamber": "Senate",
          "congress": "119",
          "cosponsors": {
            "count": "1",
            "countIncludingWithdrawnCosponsors": "1",
            "item": {
              "bioguideId": "W000817",
              "firstName": "Elizabeth",
              "fullName": "Sen. Warren, Elizabeth [D-MA]",
              "isOriginalCosponsor": "True",
              "lastName": "Warren",
              "middleName": "A.",
              "party": "D",
              "sponsorshipDate": "2025-10-09",
              "state": "MA"
            }
          },
          "number": "3930",
          "sponsors": {
            "item": {
              "bioguideId": "R000122",
              "firstName": "John",
              "fullName": "Sen. Reed, Jack [D-RI]",
              "lastName": "Reed",
              "middleName": "F.",
              "party": "D",
              "state": "RI"
            }
          },
          "submittedDate": "2025-10-09T04:00:00Z",
          "textVersions": {
            "count": "1"
          },
          "type": "SAMDT",
          "updateDate": "2025-10-09T18:10:01Z"
        }
      ]
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
            "date": "2025-03-18T17:01:37Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-13T18:36:21Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-06T15:47:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "ID"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "SD"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NC"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "LA"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "TN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "WY"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "AL"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NE"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "ND"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "OH"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s875is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 875\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Scott of South Carolina (for himself, Mr. Crapo , Mr. Rounds , Mr. Tillis , Mr. Kennedy , Mr. Hagerty , Ms. Lummis , Mrs. Britt , Mr. Ricketts , Mr. Cramer , Mr. Moreno , Mr. McCormick , and Mr. Banks ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo curtail the political weaponization of Federal banking agencies by eliminating reputational risk as a component of the supervision of depository institutions.\n#### 1. Short title\nThis Act may be cited as the Financial Integrity and Regulation Management Act or the FIRM Act .\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe primary objective of financial regulation and supervision by the Federal banking agencies is to promote safety and soundness of depository institutions;\n**(2)**\nall federally legal businesses and law-abiding citizens regardless of political ideology should have equal opportunity to obtain financial services and should not face unlawful discrimination in obtaining such services;\n**(3)**\nfinancial service providers are private entities entitled to provide services to whichever customers they so choose, provided that those decisions do not violate the law;\n**(4)**\nfinancial service providers should strive to ensure that all business decisions are based on factors free from unlawful prejudice or political influence;\n**(5)**\nthe use of reputational risk in supervisory frameworks encourages Federal banking agencies to regulate depository institutions based on the subjective view of negative publicity and provides cover for the agencies to implement their own political agenda unrelated to the safety and soundness of a depository institution;\n**(6)**\nFederal banking agencies have in fact used reputational risk to limit access of federally legal businesses and law-abiding citizens to financial services in 2018 when the Federal Deposit Insurance Corporation acknowledged that the agency used reputational risk reviews to limit access to financial services by certain industries, commonly known as Operation Choke Point ; and\n**(7)**\nreputational risk does not appear in any statute and is an unnecessary and improper use of supervisory authority that does not contribute to the safety and soundness of the financial system.\n#### 3. Definitions\nIn this Act:\n**(1) Depository institution**\nThe term depository institution \u2014\n**(A)**\nhas the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nincludes an insured credit union.\n**(2) Federal banking agency**\nThe term Federal banking agency \u2014\n**(A)**\nhas the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nincludes\u2014\n**(i)**\nthe National Credit Union Administration; and\n**(ii)**\nthe Bureau of Consumer Financial Protection.\n**(3) Insured credit union**\nThe term insured credit union has the meaning given the term in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) Reputational risk**\nThe term reputational risk means the potential that negative publicity or negative public opinion regarding an institution\u2019s business practices, whether true or not, will cause a decline in confidence in the institution or a decline in the customer base, costly litigation, or revenue reductions or otherwise adversely impact the depository institution.\n#### 4. Removal of reputational risk as a consideration in the supervision of depository institutions\nEach Federal banking agency shall remove from any guidance, rule, examination manual, or similar document established by the agency any reference to reputational risk, or any term substantially similar, regarding the supervision of depository institutions such that reputational risk, or any term substantially similar, is no longer taken into consideration by the Federal banking agency when examining and supervising a depository institution.\n#### 5. Prohibition\nNo Federal banking agency may engage in any activity concerning or related to the regulation, supervision, or examination, of the reputational risk, or any term substantially similar, or the management thereof, of a depository institution, including\u2014\n**(1)**\nestablishing any rule, regulation, requirement, standard, or supervisory expectation concerning or related to the reputational risk, or any term substantially similar, or the management thereof, of a depository institution whether binding or not;\n**(2)**\nconducting any examination, assessment, data collection, or other supervisory exercise concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution;\n**(3)**\nissuing any examination finding, supervisory criticism, or other supervisory or examination communication concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution;\n**(4)**\nmaking any supervisory ratings decision or determination that is based, in whole or in part, on any matter concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution; and\n**(5)**\ntaking any formal or informal enforcement action that is based, in whole or in part, on any matter concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution.\n#### 6. Reports\nNot later than 180 days after the date of enactment of this Act, each Federal banking agency shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report that\u2014\n**(1)**\nconfirms implementation of this Act; and\n**(2)**\ndescribes any changes made to internal policies as a result of this Act.",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s875rs.xml",
      "text": "II\nCalendar No. 32\n119th CONGRESS\n1st Session\nS. 875\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Scott of South Carolina (for himself, Mr. Crapo , Mr. Rounds , Mr. Tillis , Mr. Kennedy , Mr. Hagerty , Ms. Lummis , Mrs. Britt , Mr. Ricketts , Mr. Cramer , Mr. Moreno , Mr. McCormick , and Mr. Banks ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nMarch 18, 2025 Reported under authority of the order of the Senate of March 14, 2025, by Mr. Scott of South Carolina , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo curtail the political weaponization of Federal banking agencies by eliminating reputational risk as a component of the supervision of depository institutions.\n#### 1. Short title\nThis Act may be cited as the Financial Integrity and Regulation Management Act or the FIRM Act .\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe primary objective of financial regulation and supervision by the Federal banking agencies is to promote safety and soundness of depository institutions;\n**(2)**\nall federally legal businesses and law-abiding citizens regardless of political ideology should have equal opportunity to obtain financial services and should not face unlawful discrimination in obtaining such services;\n**(3)**\nfinancial service providers are private entities entitled to provide services to whichever customers they so choose, provided that those decisions do not violate the law;\n**(4)**\nfinancial service providers should strive to ensure that all business decisions are based on factors free from unlawful prejudice or political influence;\n**(5)**\nthe use of reputational risk in supervisory frameworks encourages Federal banking agencies to regulate depository institutions based on the subjective view of negative publicity and provides cover for the agencies to implement their own political agenda unrelated to the safety and soundness of a depository institution;\n**(6)**\nFederal banking agencies have in fact used reputational risk to limit access of federally legal businesses and law-abiding citizens to financial services in 2018 when the Federal Deposit Insurance Corporation acknowledged that the agency used reputational risk reviews to limit access to financial services by certain industries, commonly known as Operation Choke Point ;\n**(7)**\nreputational risk does not appear in any statute and is an unnecessary and improper use of supervisory authority that does not contribute to the safety and soundness of the financial system.\n#### 3. Definitions\nIn this Act:\n**(1) Depository institution**\nThe term depository institution \u2014\n**(A)**\nhas the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nincludes an insured credit union.\n**(2) Federal banking agency**\nThe term Federal banking agency \u2014\n**(A)**\nhas the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nincludes\u2014\n**(i)**\nthe National Credit Union Administration; and\n**(ii)**\nthe Bureau of Consumer Financial Protection.\n**(3) Insured credit union**\nThe term insured credit union has the meaning given the term in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) Reputational risk**\nThe term reputational risk means the potential that negative publicity or negative public opinion regarding an institution\u2019s business practices, whether true or not, will cause a decline in confidence in the institution or a decline in the customer base, costly litigation, or revenue reductions or otherwise adversely impact the depository institution.\n#### 4. Removal of reputational risk as a consideration in the supervision of depository institutions\nEach Federal banking agency shall remove from any guidance, rule, examination manual, or similar document established by the agency any reference to reputational risk, or any term substantially similar, regarding the supervision of depository institutions such that reputational risk, or any term substantially similar, is no longer taken into consideration by the Federal banking agency when examining and supervising a depository institution.\n#### 5. Prohibition\nNo Federal banking agency may engage in any activity concerning or related to the regulation, supervision, or examination, of the reputational risk, or any term substantially similar, or the management thereof, of a depository institution, including\u2014\n**(1)**\nestablishing any rule, regulation, requirement, standard, or supervisory expectation concerning or related to the reputational risk, or any term substantially similar, or the management thereof, of a depository institution whether binding or not;\n**(2)**\nconducting any examination, assessment, data collection, or other supervisory exercise concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution;\n**(3)**\nissuing any examination finding, supervisory criticism, or other supervisory or examination communication concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution;\n**(4)**\nmaking any supervisory ratings decision or determination that is based, in whole or in part, on any matter concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution; and\n**(5)**\ntaking any formal or informal enforcement action that is based, in whole or in part, on any matter concerning or related to reputational risk, or any term substantially similar, or the management thereof, of a depository institution.\n#### 6. Reports\nNot later than 180 days after the date of enactment of this Act, each Federal banking agency shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report that\u2014\n**(1)**\nconfirms implementation of this Act; and\n**(2)**\ndescribes any changes made to internal policies as a result of this Act.",
      "versionDate": "2025-03-18",
      "versionType": "Reported in Senate"
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
        "actionDate": "2026-03-04",
        "text": "Ordered to be Reported by the Yeas and Nays: 26 - 16."
      },
      "number": "6955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Capital Access Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-20",
        "text": "Placed on the Union Calendar, Calendar No. 131."
      },
      "number": "2702",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FIRM Act",
      "type": "HR"
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-04-02T14:19:44Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-02T14:35:37Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-04-02T14:35:18Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-02T14:36:06Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-02T14:35:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-23T11:21:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119s875",
          "measure-number": "875",
          "measure-type": "s",
          "orig-publish-date": "2025-03-06",
          "originChamber": "SENATE",
          "update-date": "2025-08-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s875v00",
            "update-date": "2025-08-27"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Financial Integrity and Regulation Management Act or the FIRM Act</strong></p><p>This bill prohibits the consideration of\u00a0reputational risk by federal banking agencies when regulating, examining, or supervising a depository institution or credit union. The bill defines <em>reputational risk</em> as the potential for negative publicity or public attention to decrease confidence in the institution, lead to litigation, reduce revenues, or result in other adverse impacts to the institution.\u00a0</p><p>Agencies must report on the implementation of this bill.\u00a0</p>"
        },
        "title": "FIRM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s875.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Financial Integrity and Regulation Management Act or the FIRM Act</strong></p><p>This bill prohibits the consideration of\u00a0reputational risk by federal banking agencies when regulating, examining, or supervising a depository institution or credit union. The bill defines <em>reputational risk</em> as the potential for negative publicity or public attention to decrease confidence in the institution, lead to litigation, reduce revenues, or result in other adverse impacts to the institution.\u00a0</p><p>Agencies must report on the implementation of this bill.\u00a0</p>",
      "updateDate": "2025-08-27",
      "versionCode": "id119s875"
    },
    "title": "FIRM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Financial Integrity and Regulation Management Act or the FIRM Act</strong></p><p>This bill prohibits the consideration of\u00a0reputational risk by federal banking agencies when regulating, examining, or supervising a depository institution or credit union. The bill defines <em>reputational risk</em> as the potential for negative publicity or public attention to decrease confidence in the institution, lead to litigation, reduce revenues, or result in other adverse impacts to the institution.\u00a0</p><p>Agencies must report on the implementation of this bill.\u00a0</p>",
      "updateDate": "2025-08-27",
      "versionCode": "id119s875"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s875is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s875rs.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FIRM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Financial Integrity and Regulation Management Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to curtail the political weaponization of Federal banking agencies by eliminating reputational risk as a component of the supervision of depository institutions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:36Z"
    },
    {
      "title": "FIRM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:23Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "FIRM Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Financial Integrity and Regulation Management Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-03-22T05:53:20Z"
    }
  ]
}
```
