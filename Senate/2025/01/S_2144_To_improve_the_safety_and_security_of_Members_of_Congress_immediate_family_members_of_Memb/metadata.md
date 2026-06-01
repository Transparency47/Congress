# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2144?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2144
- Title: A bill to improve the safety and security of Members of Congress, immediate family members of Members of Congress, and congressional staff.
- Congress: 119
- Bill type: S
- Bill number: 2144
- Origin chamber: Senate
- Introduced date: 2025-06-23
- Update date: 2026-03-12T15:09:20Z
- Update date including text: 2026-03-12T15:09:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in Senate
- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-09-29 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S6844)
- 2025-09-29 - Floor: Passed Senate with an amendment by Unanimous Consent. (text: CR S6841-6842)
- 2025-09-29 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-09-29 - Discharge: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2025-09-29 - Committee: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2025-10-08 - Floor: Message on Senate action sent to the House.
- 2025-10-10 12:33:04 - Floor: Received in the House.
- 2025-10-10 12:33:05 - Floor: Held at the desk.
- Latest action: 2025-06-23: Introduced in Senate

## Actions

- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-09-29 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S6844)
- 2025-09-29 - Floor: Passed Senate with an amendment by Unanimous Consent. (text: CR S6841-6842)
- 2025-09-29 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-09-29 - Discharge: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2025-09-29 - Committee: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2025-10-08 - Floor: Message on Senate action sent to the House.
- 2025-10-10 12:33:04 - Floor: Received in the House.
- 2025-10-10 12:33:05 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2144",
    "number": "2144",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A bill to improve the safety and security of Members of Congress, immediate family members of Members of Congress, and congressional staff.",
    "type": "S",
    "updateDate": "2026-03-12T15:09:20Z",
    "updateDateIncludingText": "2026-03-12T15:09:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-10-10",
      "actionTime": "12:33:05",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-10-10",
      "actionTime": "12:33:04",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (text: CR S6841-6842)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S6844)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-23",
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
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2025-09-29",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 3916 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2025-09-29",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 3916 proposed by Senator Thune for Senator Klobuchar. In the nature of a substitute.",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-09-29",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-09-29",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "93000",
                "actionDate": "2025-09-29",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 3916 proposed by Senator Thune for Senator Klobuchar.",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2025-09-29",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 3916 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "2144",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "A bill to improve the safety and security of Members of Congress, immediate family members of Members of Congress, and congressional staff.",
          "type": "S",
          "updateDateIncludingText": "2026-03-12"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2025-09-29",
          "links": {
            "link": {
              "name": "SA 3916",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/3916"
            }
          },
          "text": "Amendment SA 3916 agreed to in Senate by Unanimous Consent."
        },
        "number": "3916",
        "onBehalfOfSponsor": {
          "item": [
            {
              "bioguideId": "T000250",
              "firstName": "John",
              "fullName": "Sen. Thune, John [R-SD]",
              "lastName": "Thune",
              "party": "R",
              "state": "SD",
              "type": "Submitted on behalf of"
            },
            {
              "bioguideId": "T000250",
              "firstName": "John",
              "fullName": "Sen. Thune, John [R-SD]",
              "lastName": "Thune",
              "party": "R",
              "state": "SD",
              "type": "Proposed on behalf of"
            }
          ]
        },
        "proposedDate": "2025-09-29T04:00:00Z",
        "purpose": "In the nature of a substitute.",
        "sponsors": {
          "item": {
            "bioguideId": "K000367",
            "firstName": "Amy",
            "fullName": "Sen. Klobuchar, Amy [D-MN]",
            "lastName": "Klobuchar",
            "party": "D",
            "state": "MN"
          }
        },
        "submittedDate": "2025-09-29T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2025-09-30T01:54:43Z"
      }
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
            "date": "2025-09-30T01:50:57Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-06-23T22:25:17Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2144is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2144\nIN THE SENATE OF THE UNITED STATES\nJune 23, 2025 Ms. Klobuchar (for herself and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo improve the safety and security of Members of Congress, immediate family members of Members of Congress, and congressional staff.\n#### 1. Protecting covered information in public records\n##### (a) Definitions\nIn this section:\n**(1) Applicable legislative officers**\nThe term applicable legislative officers means\u2014\n**(A)**\nwith respect to a Member of the Senate, the Sergeant at Arms and Doorkeeper of the Senate and the Secretary of the Senate, acting jointly; and\n**(B)**\nwith respect to a Member of, or Delegate or Resident Commissioner to, the House of Representatives, the Sergeant at Arms of the House of Representatives and the Chief Administrative Officer of the House of Representatives, acting jointly.\n**(2) At-risk individual**\nThe term at-risk individual means\u2014\n**(A)**\na Member of Congress;\n**(B)**\nany individual who is the spouse, parent, sibling, or child of an individual described in subparagraph (A);\n**(C)**\nany individual to whom an individual described in subparagraph (A) stands in loco parentis;\n**(D)**\nany other individual living in the household of an individual described in subparagraph (A);\n**(E)**\nany employee whose pay is disbursed by the Secretary of the Senate who is identified by the Director of Senate Security as the target of an ongoing threat; or\n**(F)**\nany employee whose pay is disbursed by the Chief Administrative Officer of the House of Representatives who is identified by the Director of the Office of House Security as the target of an ongoing threat.\n**(3) Covered information**\nThe term covered information means\u2014\n**(A)**\na home address, including a primary residence or secondary residences;\n**(B)**\na home or personal mobile telephone number;\n**(C)**\na personal email address;\n**(D)**\na social security number or driver\u2019s license number;\n**(E)**\na bank account or credit or debit card number;\n**(F)**\na license plate number or other unique identifier of a vehicle owned, leased, or regularly used by an at-risk individual;\n**(G)**\nthe identification of a child, who is under 18 years of age, of an at-risk individual;\n**(H)**\ninformation regarding current or future school or day care attendance, including the name or addresses of the school or day care;\n**(I)**\ninformation regarding schedules of school or day care attendance or routes taken to or from the school or day care by an at-risk individual;\n**(J)**\ninformation regarding routes taken to or from an employment location by an at-risk individual; or\n**(K)**\nprecise geolocation data that is not anonymized and can identify the location of a device of an at-risk individual.\n**(4) Data broker**\n**(A) In general**\nThe term data broker means a commercial entity engaged in collecting, assembling, or maintaining personal information concerning an individual who is not a customer, client, or an employee of that entity in order to sell the information or otherwise profit from providing third-party access to the information.\n**(B) Exclusion**\nThe term data broker does not include a commercial entity engaged in the following activities:\n**(i)**\nEngaging in reporting, news-gathering, speaking, or other activities intended to inform the public on matters of public interest or public concern.\n**(ii)**\nProviding 411 directory assistance or directory information services, including name, address, and telephone number, on behalf of or as a function of a telecommunications carrier.\n**(iii)**\nUsing personal information internally, providing access to businesses under common ownership or affiliated by corporate control, or selling or providing data for a transaction or service requested by or concerning the individual whose personal information is being transferred.\n**(iv)**\nProviding publicly available information via real-time or near-real-time alert services for health or safety purposes.\n**(v)**\nA consumer reporting agency subject to the Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ).\n**(vi)**\nA financial institution subject to the Gramm-Leach-Bliley Act ( Public Law 106\u2013102 ) and regulations implementing that Act.\n**(vii)**\nA covered entity for purposes of the privacy regulations promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996 ( 42 U.S.C. 1320d\u20132 note).\n**(viii)**\nThe collection and sale or licensing of covered information incidental to conducting the activities described in clauses (i) through (vii).\n**(5) Government agency**\nThe term Government agency includes\u2014\n**(A)**\nan Executive agency, as defined in section 105 of title 5, United States Code; and\n**(B)**\nany agency in the judicial branch or legislative branch.\n**(6) Immediate family member**\nThe term immediate family member means an at-risk individual\u2014\n**(A)**\nwho is the spouse, parent, sibling, or child of another at-risk individual;\n**(B)**\nto whom another at-risk individual stands in loco parentis; or\n**(C)**\nliving in the household of another at-risk individual.\n**(7) Member of Congress**\nThe term Member of Congress means\u2014\n**(A)**\na Member of the Senate; or\n**(B)**\na Member of, or Delegate or Resident Commissioner to, the House of Representatives.\n**(8) Transfer**\nThe term transfer means to sell, license, trade, or exchange for consideration the covered information of an at-risk individual.\n##### (b) Government agencies\n**(1) In general**\nEach at-risk individual may\u2014\n**(A)**\nfile written notice of the status of the individual as an at-risk individual, for themselves and their immediate family members, with each Government agency that includes information necessary to ensure compliance with this section, as determined by the applicable legislative officers; and\n**(B)**\nrequest that each Government agency described in subparagraph (A) mark as private their covered information and that of their immediate family members.\n**(2) No public posting**\n**(A) In general**\nGovernment agencies shall not publicly post or display publicly available content that includes covered information of an at-risk individual.\n**(B) Deadline**\nUpon receipt of a request by an at-risk individual under paragraph (1)(B), a Government agency shall remove the covered information of the at-risk individual, and any immediate family member on whose behalf the at-risk individual submitted the request, from publicly available content not later than 72 hours after such receipt.\n**(3) Exceptions**\nNothing in this section shall prohibit a Government agency from providing access to records containing the covered information of an at-risk individual to a third party if the third party\u2014\n**(A)**\npossesses a signed release from the at-risk individual or a court order;\n**(B)**\nis subject to the requirements of title V of the Gramm-Leach-Bliley Act ( 15 U.S.C. 6801 et seq. ); or\n**(C)**\nexecutes a confidentiality agreement with the Government agency.\n##### (c) Delegation of authority\n**(1) In general**\nAn at-risk individual may directly, or through an agent designated by the at-risk individual, make any notice or request required or authorized by this section on behalf of the at-risk individual. The notice or request shall include information necessary to ensure compliance with this section.\n**(2) Authorization of legislative officers to make requests**\n**(A) Legislative officers**\nUpon written request of a Member of Congress, the applicable legislative officers are authorized to make any notice or request required or authorized by this section on behalf of the Member of Congress. The notice or request shall include information necessary to ensure compliance with this section, as determined by the applicable legislative officers. Any notice or request made under this paragraph shall be deemed to have been made by the Member of Congress and comply with the notice and request requirements of this section.\n**(B) List**\nIn lieu of individual notices or requests, the applicable legislative officers may provide Government agencies, data brokers, persons, businesses, or associations with a list of Members of Congress and their immediate family members that includes information necessary to ensure compliance with this section, as determined by the applicable legislative officers for the purpose of maintaining compliance with this section. Such list shall be deemed to comply with individual notice and request requirements of this section.\n##### (d) Data brokers and other businesses\n**(1) Prohibitions**\n**(A) Data brokers**\nIt shall be unlawful for a data broker to knowingly sell, license, trade for consideration, or purchase covered information of an at-risk individual.\n**(B) Other businesses**\n**(i) In general**\nExcept as provided in clause (ii), no person, business, or association shall publicly post or publicly display on the internet covered information of an at-risk individual if the at-risk individual, or an immediate family member on behalf of the at-risk individual, has made a written request to that person, business, or association to not disclose the covered information of the at-risk individual.\n**(ii) Exceptions**\nClause (i) shall not apply to\u2014\n**(I)**\nthe display on the internet of the covered information of an at-risk individual if the information is relevant to and displayed as part of a news story, commentary, editorial, or other speech on a matter of public concern;\n**(II)**\ncovered information that the at-risk individual voluntarily publishes on the internet after the date of enactment of this Act; or\n**(III)**\ncovered information received from a Federal Government source (or from an employee or agent of the Federal Government).\n**(2) Required conduct**\n**(A) In general**\nAfter receiving a written request under paragraph (1)(B)(i), the person, business, or association shall\u2014\n**(i)**\nremove within 72 hours the covered information from the internet and ensure that the information is not made available on any website or subsidiary website controlled by that person, business, or association; and\n**(ii)**\nensure that the covered information of the at-risk individual is not made available on any website or subsidiary website controlled by that person, business, or association.\n**(B) Transfer**\n**(i) In general**\nExcept as provided in clause (ii), after receiving a written request under paragraph (1)(B)(i), the person, business, or association shall not transfer the covered information of the at-risk individual to any other person, business, or association through any medium.\n**(ii) Exceptions**\nClause (i) shall not apply to\u2014\n**(I)**\nthe transfer of the covered information of the at-risk individual if the information is relevant to and displayed as part of a news story, commentary, editorial, or other speech on a matter of public concern;\n**(II)**\ncovered information that the at-risk individual voluntarily publishes on the internet after the date of enactment of this Act; or\n**(III)**\na transfer made at the request of the at-risk individual or that is necessary to effectuate a request to the person, business, or association from the at-risk individual.\n##### (e) Redress\nAn at-risk individual whose covered information is made public as a result of a violation of this section may bring an action seeking injunctive or declaratory relief in any court of competent jurisdiction.\n##### (f) Rules of construction\n**(1) In general**\nNothing in this section shall be construed\u2014\n**(A)**\nto prohibit, restrain, or limit\u2014\n**(i)**\nthe lawful investigation or reporting by the press of any unlawful activity or misconduct alleged to have been committed by an at-risk individual;\n**(ii)**\nthe reporting on an at-risk individual regarding matters of public concern; or\n**(iii)**\nthe disclosure of information otherwise required under Federal law;\n**(B)**\nto impair access to the actions or statements of a Member of Congress in the course of carrying out the public functions of the Member of Congress;\n**(C)**\nto limit the publication or transfer of covered information with the written consent of the at-risk individual; or\n**(D)**\nto prohibit information sharing by a data broker to a Federal, State, Tribal, or local government, or any unit thereof.\n**(2) Protection of covered information**\nThis section shall be broadly construed to favor the protection of the covered information of at-risk individuals.\n##### (g) Severability\nIf any provision of this section, or the application of such provision to any person or circumstance, is held to be unconstitutional, the remaining provisions of this section, and the application of the provision to any other person or circumstance, shall not be affected.",
      "versionDate": "2025-06-23",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2144es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 2144\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo improve the safety and security of Members of Congress, immediate family members of Members of Congress, and congressional staff.\n#### 1. Protecting covered information in public records\n##### (a) Definitions\nIn this section:\n**(1) Applicable legislative officers**\nThe term applicable legislative officers means\u2014\n**(A)**\nwith respect to a Member of the Senate or a designated Senate employee, the Sergeant at Arms and Doorkeeper of the Senate and the Secretary of the Senate, acting jointly; and\n**(B)**\nwith respect to a Member of, or Delegate or Resident Commissioner to, the House of Representatives or a designated House employee, the Sergeant at Arms of the House of Representatives and the Chief Administrative Officer of the House of Representatives, acting jointly.\n**(2) At-risk individual**\nThe term at-risk individual means\u2014\n**(A)**\na Member of Congress;\n**(B)**\nany individual who is the spouse, parent, sibling, or child of an individual described in subparagraph (A);\n**(C)**\nany individual to whom an individual described in subparagraph (A) stands in loco parentis;\n**(D)**\nany other individual living in the household of an individual described in subparagraph (A);\n**(E)**\nany designated Senate employee;\n**(F)**\nany designated House employee; or\n**(G)**\na former Member of Congress.\n**(3) Candidate**\nThe term candidate has the meaning given the term in section 301 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 ).\n**(4) Covered employee**\nThe term covered employee has the same meaning given such term in section 101 of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 ).\n**(5) Covered information**\nThe term covered information \u2014\n**(A)**\nmeans\u2014\n**(i)**\na home address, including a primary residence or secondary residences;\n**(ii)**\na home or personal mobile telephone number;\n**(iii)**\na personal email address;\n**(iv)**\na social security number or driver\u2019s license number;\n**(v)**\na bank account or credit or debit card number;\n**(vi)**\na license plate number or other unique identifier of a vehicle owned, leased, or regularly used by an at-risk individual;\n**(vii)**\nthe identification of a child, who is under 18 years of age, of an at-risk individual;\n**(viii)**\ninformation regarding current or future school or day care attendance, including the name or addresses of the school or day care;\n**(ix)**\ninformation regarding schedules of school or day care attendance or routes taken to or from the school or day care by an at-risk individual;\n**(x)**\ninformation regarding routes taken to or from an employment location by an at-risk individual; or\n**(xi)**\nprecise geolocation data that is not anonymized and can identify the location of a device of an at-risk individual; and\n**(B)**\ndoes not include information described in subparagraph (A) that is contained in\u2014\n**(i)**\nany report or other record required to be filed with the Federal Election Commission; or\n**(ii)**\nany report or other record otherwise required under Federal or State law to be filed\u2014\n**(I)**\nby an individual to qualify as a candidate for the office of Member of Congress; or\n**(II)**\nby any candidate for the office of Member of Congress.\n**(6) Data broker**\n**(A) In general**\nThe term data broker means a commercial entity engaged in collecting, assembling, or maintaining personal information concerning an individual who is not a customer, client, or an employee of that entity in order to sell the information or otherwise profit from providing third-party access to the information.\n**(B) Exclusion**\nThe term data broker does not include a commercial entity engaged in the following activities:\n**(i)**\nEngaging in reporting, news-gathering, speaking, or other activities intended to inform the public on matters of public interest or public concern.\n**(ii)**\nProviding 411 directory assistance or directory information services, including name, address, and telephone number, on behalf of or as a function of a telecommunications carrier.\n**(iii)**\nUsing personal information internally, providing access to businesses under common ownership or affiliated by corporate control, or selling or providing data for a transaction or service requested by or concerning the individual whose personal information is being transferred.\n**(iv)**\nProviding publicly available information via real-time or near-real-time alert services for health or safety purposes.\n**(v)**\nA consumer reporting agency, only while engaging in activity subject to the Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ).\n**(vi)**\nA financial institution subject to the Gramm-Leach-Bliley Act ( Public Law 106\u2013102 ) and regulations implementing that Act.\n**(vii)**\nA covered entity for purposes of the privacy regulations promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996 ( 42 U.S.C. 1320d\u20132 note).\n**(viii)**\nThe collection and sale or licensing of covered information incidental to conducting the activities described in clauses (i) through (vii).\n**(7) Designated House employee**\nThe term designated House employee means\u2014\n**(A)**\na covered employee designated in writing by\u2014\n**(i)**\na Member of, or Delegate or Resident Commissioner to, the House of Representatives; or\n**(ii)**\nan officer of the House of Representatives; or\n**(B)**\nan officer of the House of Representatives.\n**(8) Designated Senate employee**\nThe term designated Senate employee means\u2014\n**(A)**\na covered employee designated in writing by\u2014\n**(i)**\na Member of the Senate; or\n**(ii)**\nan officer of the Senate; or\n**(B)**\nan officer of the Senate.\n**(9) Government agency**\nThe term Government agency includes\u2014\n**(A)**\nan Executive agency, as defined in section 105 of title 5, United States Code; and\n**(B)**\nany agency in the judicial branch or legislative branch.\n**(10) Immediate family member**\nThe term immediate family member means an at-risk individual\u2014\n**(A)**\nwho is the spouse, parent, sibling, or child of another at-risk individual;\n**(B)**\nto whom another at-risk individual stands in loco parentis; or\n**(C)**\nliving in the household of another at-risk individual.\n**(11) Member of Congress**\nThe term Member of Congress means\u2014\n**(A)**\na Member of the Senate; or\n**(B)**\na Member of, or Delegate or Resident Commissioner to, the House of Representatives.\n**(12) Transfer**\nThe term transfer means to sell, license, trade, or exchange for consideration the covered information of an at-risk individual.\n##### (b) Government agencies\n**(1) In general**\nEach at-risk individual may\u2014\n**(A)**\nfile written notice of the status of the individual as an at-risk individual, for themselves and their immediate family members, with each Government agency that includes information necessary to ensure compliance with this section, as determined by the applicable legislative officers; and\n**(B)**\nrequest that each Government agency described in subparagraph (A) mark as private their covered information and that of their immediate family members.\n**(2) No public posting**\n**(A) In general**\nGovernment agencies shall not publicly post or display publicly available content that includes covered information of an at-risk individual.\n**(B) Deadline**\nUpon receipt of a request by an at-risk individual under paragraph (1)(B), a Government agency shall remove the covered information of the at-risk individual, and any immediate family member on whose behalf the at-risk individual submitted the request, from publicly available content not later than 72 hours after such receipt.\n**(3) Exceptions**\nNothing in this section shall prohibit a Government agency from providing access to records containing the covered information of an at-risk individual to a third party if the third party\u2014\n**(A)**\npossesses a signed release from the at-risk individual or a court order;\n**(B)**\nis subject to the requirements of title V of the Gramm-Leach-Bliley Act ( 15 U.S.C. 6801 et seq. ); or\n**(C)**\nexecutes a confidentiality agreement with the Government agency.\n##### (c) Delegation of authority\n**(1) In general**\nAn at-risk individual may directly, or through an agent designated by the at-risk individual, make any notice or request required or authorized by this section on behalf of the at-risk individual. The notice or request shall include information necessary to ensure compliance with this section.\n**(2) Authorization of legislative officers and employees to make requests**\n**(A) Legislative officers**\nUpon written request of a Member of Congress, designated Senate employee, or designated House employee, the applicable legislative officers are authorized to make any notice or request required or authorized by this section on behalf of the Member of Congress, designated Senate employee, or designated House employee, respectively. The notice or request shall include information necessary to ensure compliance with this section, as determined by the applicable legislative officers. Any notice or request made under this subparagraph shall be deemed to have been made by the Member of Congress, designated Senate employee, or designated House employee, as applicable, and comply with the notice and request requirements of this section.\n**(B) List**\n**(i) In general**\nIn lieu of individual notices or requests, the applicable legislative officers may provide Government agencies, data brokers, persons, businesses, or associations with a list of\u2014\n**(I)**\nMembers of Congress, designated Senate employees, and designated House employees making a written request described in subparagraph (A); and\n**(II)**\nimmediate family members of the Members of Congress, designated Senate employees, and designated House employees on whose behalf the written request was made.\n**(ii) Contents**\nA list provided under clause (i) shall include information necessary to ensure compliance with this section, as determined by the applicable legislative officers for the purpose of maintaining compliance with this section.\n**(iii) Compliance with notice and request requirement**\nA list provided under clause (i) shall be deemed to comply with individual notice and request requirements of this section.\n##### (d) Data brokers and other businesses\n**(1) Prohibitions**\n**(A) Data brokers**\nIt shall be unlawful for a data broker to knowingly sell, license, trade for consideration, or purchase covered information of an at-risk individual.\n**(B) Other businesses**\n**(i) In general**\nExcept as provided in clause (ii), no person, business, or association shall publicly post or publicly display on the internet covered information of an at-risk individual if the at-risk individual, or an immediate family member on behalf of the at-risk individual, has made a written request to that person, business, or association to not disclose the covered information of the at-risk individual.\n**(ii) Exceptions**\nClause (i) shall not apply to\u2014\n**(I)**\nthe display on the internet of the covered information of an at-risk individual if the information is relevant to and displayed as part of a news story, commentary, editorial, or other speech on a matter of public concern;\n**(II)**\ncovered information that the at-risk individual voluntarily publishes on the internet after the date of enactment of this Act; or\n**(III)**\ncovered information lawfully received from a Federal Government source (or from an employee or agent of the Federal Government).\n**(2) Required conduct**\n**(A) In general**\nAfter receiving a written request under paragraph (1)(B)(i), the person, business, or association shall\u2014\n**(i)**\nremove within 72 hours the covered information from the internet and ensure that the information is not made available on any website or subsidiary website controlled by that person, business, or association; and\n**(ii)**\nensure that the covered information of the at-risk individual is not made available on any website or subsidiary website controlled by that person, business, or association.\n**(B) Transfer**\n**(i) In general**\nExcept as provided in clause (ii), after receiving a written request under paragraph (1)(B)(i), the person, business, or association shall not transfer the covered information of the at-risk individual to any other person, business, or association through any medium.\n**(ii) Exceptions**\nClause (i) shall not apply to\u2014\n**(I)**\nthe transfer of the covered information of the at-risk individual if the information is relevant to and displayed as part of a news story, commentary, editorial, or other speech on a matter of public concern;\n**(II)**\ncovered information that the at-risk individual voluntarily publishes on the internet after the date of enactment of this Act; or\n**(III)**\na transfer made at the request of the at-risk individual or that is necessary to effectuate a request to the person, business, or association from the at-risk individual.\n##### (e) Redress\nAn at-risk individual whose covered information is made public as a result of a violation of this section may bring an action seeking injunctive or declaratory relief in any court of competent jurisdiction.\n##### (f) Rules of construction\n**(1) In general**\nNothing in this section shall be construed\u2014\n**(A)**\nto prohibit, restrain, or limit\u2014\n**(i)**\nthe lawful investigation or reporting by the press of any unlawful activity or misconduct alleged to have been committed by an at-risk individual;\n**(ii)**\nthe reporting on an at-risk individual regarding matters of public concern; or\n**(iii)**\nthe disclosure of information otherwise required under Federal law;\n**(B)**\nto impair access to the actions or statements of a Member of Congress in the course of carrying out the public functions of the Member of Congress;\n**(C)**\nto limit the publication or transfer of covered information with the written consent of the at-risk individual; or\n**(D)**\nto prohibit information sharing by a data broker to a Federal, State, Tribal, or local government, or any unit thereof.\n**(2) Protection of covered information**\nThis section shall be broadly construed to favor the protection of the covered information of at-risk individuals.\n##### (g) Severability\nIf any provision of this section, or the application of such provision to any person or circumstance, is held to be unconstitutional, the remaining provisions of this section, and the application of the provision to any other person or circumstance, shall not be affected.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-09-17",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2851",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Americans from Doxing and Political Violence Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-17",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2850",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Legislators and Survivors of Sexual Assault and Domestic Violence from Doxing and Political Violence Act",
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
            "name": "Computer security and identity theft",
            "updateDate": "2025-09-30T17:55:44Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-09-30T17:55:57Z"
          },
          {
            "name": "Congressional officers and employees",
            "updateDate": "2025-09-30T17:54:18Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-30T17:56:38Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-09-30T17:53:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-07-15T11:15:56Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2144is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2144es.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the safety and security of Members of Congress, immediate family members of Members of Congress, and congressional staff.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-04T02:18:39Z"
    },
    {
      "title": "A bill to improve the safety and security of Members of Congress, immediate family members of Members of Congress, and congressional staff.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T10:56:20Z"
    }
  ]
}
```
