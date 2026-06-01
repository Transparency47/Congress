# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/161?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/161
- Title: She DRIVES Act
- Congress: 119
- Bill type: S
- Bill number: 161
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2026-03-12T16:03:59Z
- Update date including text: 2026-03-12T16:03:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-07-31 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-56.
- 2025-07-31 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-56.
- 2025-07-31 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 141.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-07-31 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-56.
- 2025-07-31 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-56.
- 2025-07-31 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 141.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/161",
    "number": "161",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "She DRIVES Act",
    "type": "S",
    "updateDate": "2026-03-12T16:03:59Z",
    "updateDateIncludingText": "2026-03-12T16:03:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 141.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-56.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-07-31",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-56.",
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
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
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
            "date": "2025-07-31T20:40:33Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T15:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-21T20:21:09Z",
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
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "WA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TN"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "IL"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "ME"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "VT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "WV"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "HI"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "AL"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "CO"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NV"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "MT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "MS"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s161is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 161\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mrs. Fischer (for herself, Mrs. Murray , Mrs. Blackburn , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Transportation to issue rules relating to the testing procedures used under the New Car Assessment Program of the National Highway Traffic Safety Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the She Develops Regulations In Vehicle Equality and Safety Act or the She DRIVES Act .\n#### 2. Definitions\nIn this Act:\n**(1) Crashworthiness**\nThe term crashworthiness has the meaning given the term in section 32301 of title 49, United States Code.\n**(2) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(3) Testing device**\nThe term testing device means a testing device used for compliance testing of motor vehicles and motor vehicle equipment with respect to Federal motor vehicle safety standards that is described in part 572 of title 49, Code of Federal Regulations (or successor regulations).\n#### 3. Federal Motor Vehicle Safety Standards updates\n##### (a) Front impacts\n**(1) In general**\nNot later than 15 days after the date of enactment of this Act, the Secretary shall revise parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations), to include the following:\n**(A)**\n50th percentile adult male Test Device for Human Occupant Restraint (THOR) frontal impact testing device.\n**(B)**\n5th percentile adult female Test Device for Human Occupant Restraint (THOR) front impact testing device.\n**(2) Front impact final rules**\n**(A) In general**\n**(i) THOR-50M**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall issue a final rule to require the use of the testing device described in paragraph (1)(A) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(ii) THOR-05F**\n**(I) Proposed rulemaking**\nNot later than 60 days after the date of enactment of this Act, the Secretary shall issue a notice of proposed rulemaking to require the use of the testing device described in paragraph (1)(B) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(II) Final rule**\nNot later than 120 days after the date of enactment of this Act, the Secretary shall issue a final rule to require the use of the testing device described in paragraph (1)(B) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(B) Requirements**\nIn issuing the final rules under clauses (i) and (ii)(II) of subparagraph (A), the Secretary shall\u2014\n**(i)**\nestablish or update the injury criteria, including the head, neck, chest, abdomen, pelvis, upper leg, and lower leg injury criteria, for the testing devices described in subparagraphs (A) and (B) of paragraph (1) based on real world injuries and the greatest potential to increase safety; and\n**(ii)**\nestablish crashworthiness frontal impact tests with those testing devices for adult female occupants in all designated front seating positions tested, as of the date of enactment of this Act, for adult male occupants.\n**(C) New car assessment program update**\n**(i) In general**\nThe Secretary shall promulgate a final decision notice to update the testing procedures used to test the crashworthiness of passenger motor vehicles under the New Car Assessment Program of the National Highway Traffic Safety Administration to require the use of the testing devices described in subparagraphs (A) and (B) of paragraph (1).\n**(ii) Timing**\n**(I) In general**\nThe final decision notice required under clause (i) shall be promulgated concurrently with the issuance of the final rule required under subparagraph (A)(i) if the Secretary determines that promulgating the final decision notice concurrently with the final rule required under that subparagraph does not delay issuance of that final rule.\n**(II) Delay**\nIf the Secretary determines under subclause (I) that promulgating the final decision notice concurrently with the final rule required under subparagraph (A)(i) would delay the issuance of that final rule, the Secretary shall issue that final rule before promulgating the final decision notice required under this subparagraph.\n##### (b) Side impacts\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, the Secretary shall revise parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations), to include the following:\n**(A)**\n50th percentile adult male Worldwide Harmonized Side Impact Dummy side impact testing device.\n**(B)**\n5th percentile adult female Worldwide Harmonized Side Impact Dummy side impact testing device.\n**(2) Side impact final rule**\n**(A) In general**\n**(i) Proposed rulemaking**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall issue a notice of proposed rulemaking to require the use of the testing devices described in subparagraphs (A) and (B) of paragraph (1) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(ii) Final rule**\nNot later than 30 months after the date of enactment of this Act, the Secretary shall issue a final rule to require the use of the testing devices described in subparagraphs (A) and (B) of paragraph (1) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(B) Requirements**\nIn issuing the final rule under subparagraph (A)(ii), the Secretary shall\u2014\n**(i)**\nestablish or update the injury criteria, including the head, neck, chest, abdomen, pelvis, and upper leg criteria, for the testing devices described in subparagraphs (A) and (B) of paragraph (1) based on real world injuries and the greatest potential to increase safety; and\n**(ii)**\nestablish front seat crashworthiness side impact tests with those testing devices for adult female occupants in all designated front seating positions tested, as of the date of enactment of this Act, for adult male occupants.\n**(C) New car assessment program update**\n**(i) In general**\nThe Secretary shall promulgate a final decision notice to update the testing procedures used to test the crashworthiness of passenger motor vehicles under the New Car Assessment Program of the National Highway Traffic Safety Administration to require the use of the testing devices described in subparagraphs (A) and (B) of paragraph (1).\n**(ii) Timing**\n**(I) In general**\nThe final decision notice required under clause (i) shall be promulgated concurrently with the issuance of the final rule required under subparagraph (A)(ii) if the Secretary determines that promulgating the final decision notice concurrently with the final rule required under that subparagraph does not delay issuance of that final rule.\n**(II) Delay**\nIf the Secretary determines under subclause (I) that promulgating the final decision notice concurrently with the final rule required under subparagraph (A)(ii) would delay the issuance of that final rule, the Secretary shall issue that final rule before promulgating the final decision notice required under this subparagraph.\n#### 4. Testing devices roadmap\n##### (a) Initial report\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that\u2014\n**(A)**\nidentifies timelines for the Secretary to incorporate testing devices, other than the testing devices described in subparagraphs (A) and (B) of section 3(a)(1) and subparagraphs (A) and (B) of section 3(b)(1), that the Secretary is researching, as of the date of enactment of this Act, into the regulations contained in parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations);\n**(B)**\nidentifies testing devices used for similar crashworthiness standards in other countries that are more advanced than the testing devices required or being researched by the Secretary; and\n**(C)**\nsubject to paragraph (2), describes a process for the Secretary to update the testing devices required in the United States under regulations in effect on the date of enactment of this Act, including whether the Secretary can adopt more advanced testing devices already used for compliance in other countries, such as testing devices in use or being considered as part of the European New Car Assessment Programme.\n**(2) No update needed**\nIf the Secretary determines that testing devices used in the United States as of the date of enactment of this Act do not need to be updated, the Secretary shall include in the report required under paragraph (1) a description for why the Secretary believes those testing devices do not need to be updated, including by providing a description for each testing device described in part 572 of title 49, Code of Federal Regulations (or successor regulations), that the Secretary determines does not need to be updated.\n##### (b) Follow-Up report\nNot later than 5 years after the date on which the Secretary submits the report required under subsection (a), the Secretary shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that\u2014\n**(1)**\ndescribes whether the Secretary has met the timelines described in subsection (a)(1)(A); and\n**(2)**\nidentifies any new testing devices used in other countries that are more advanced than the testing devices required or being research by the Secretary as of the date of enactment of this Act.",
      "versionDate": "2025-01-21",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s161rs.xml",
      "text": "II\nCalendar No. 141\n119th CONGRESS\n1st Session\nS. 161\n[Report No. 119\u201356]\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mrs. Fischer (for herself, Mrs. Murray , Mrs. Blackburn , Ms. Duckworth , Ms. Collins , Mr. Welch , Mrs. Capito , Mr. Schatz , Mrs. Britt , Mr. Hickenlooper , Ms. Rosen , and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nJuly 31, 2025 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require the Secretary of Transportation to issue rules relating to the testing procedures used under the New Car Assessment Program of the National Highway Traffic Safety Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the She Develops Regulations In Vehicle Equality and Safety Act or the She DRIVES Act .\n#### 2. Definitions\nIn this Act:\n**(1) Crashworthiness**\nThe term crashworthiness has the meaning given the term in section 32301 of title 49, United States Code.\n**(2) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(3) Testing device**\nThe term testing device means a testing device used for compliance testing of motor vehicles and motor vehicle equipment with respect to Federal motor vehicle safety standards that is described in part 572 of title 49, Code of Federal Regulations (or successor regulations).\n#### 3. Federal Motor Vehicle Safety Standards updates\n##### (a) Front impacts\n**(1) In general**\nNot later than 15 days after the date of enactment of this Act, the Secretary shall revise parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations), to include the following:\n**(A)**\n50th percentile adult male Test Device for Human Occupant Restraint (THOR) frontal impact testing device.\n**(B)**\n5th percentile adult female Test Device for Human Occupant Restraint (THOR) front impact testing device.\n**(2) Front impact final rules**\n**(A) In general**\n**(i) THOR-50M**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall issue a final rule to require the use of the testing device described in paragraph (1)(A) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(ii) THOR-05F**\n**(I) Proposed rulemaking**\nNot later than 60 days after the date of enactment of this Act, the Secretary shall issue a notice of proposed rulemaking to require the use of the testing device described in paragraph (1)(B) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(II) Final rule**\nNot later than 120 days after the date of enactment of this Act, the Secretary shall issue a final rule to require the use of the testing device described in paragraph (1)(B) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(B) Requirements**\nIn issuing the final rules under clauses (i) and (ii)(II) of subparagraph (A), the Secretary shall\u2014\n**(i)**\nestablish or update the injury criteria, including the head, neck, chest, abdomen, pelvis, upper leg, and lower leg injury criteria, for the testing devices described in subparagraphs (A) and (B) of paragraph (1) based on real world injuries and the greatest potential to increase safety; and\n**(ii)**\nestablish crashworthiness frontal impact tests with those testing devices for adult female occupants in all designated front seating positions tested, as of the date of enactment of this Act, for adult male occupants.\n**(C) New car assessment program update**\n**(i) In general**\nThe Secretary shall promulgate a final decision notice to update the testing procedures used to test the crashworthiness of passenger motor vehicles under the New Car Assessment Program of the National Highway Traffic Safety Administration to require the use of the testing devices described in subparagraphs (A) and (B) of paragraph (1).\n**(ii) Timing**\n**(I) In general**\nThe final decision notice required under clause (i) shall be promulgated concurrently with the issuance of the final rule required under subparagraph (A)(i) if the Secretary determines that promulgating the final decision notice concurrently with the final rule required under that subparagraph does not delay issuance of that final rule.\n**(II) Delay**\nIf the Secretary determines under subclause (I) that promulgating the final decision notice concurrently with the final rule required under subparagraph (A)(i) would delay the issuance of that final rule, the Secretary shall issue that final rule before promulgating the final decision notice required under this subparagraph.\n##### (b) Side impacts\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, the Secretary shall revise parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations), to include the following:\n**(A)**\n50th percentile adult male Worldwide Harmonized Side Impact Dummy side impact testing device.\n**(B)**\n5th percentile adult female Worldwide Harmonized Side Impact Dummy side impact testing device.\n**(2) Side impact final rule**\n**(A) In general**\n**(i) Proposed rulemaking**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall issue a notice of proposed rulemaking to require the use of the testing devices described in subparagraphs (A) and (B) of paragraph (1) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(ii) Final rule**\nNot later than 30 months after the date of enactment of this Act, the Secretary shall issue a final rule to require the use of the testing devices described in subparagraphs (A) and (B) of paragraph (1) into parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations).\n**(B) Requirements**\nIn issuing the final rule under subparagraph (A)(ii), the Secretary shall\u2014\n**(i)**\nestablish or update the injury criteria, including the head, neck, chest, abdomen, pelvis, and upper leg criteria, for the testing devices described in subparagraphs (A) and (B) of paragraph (1) based on real world injuries and the greatest potential to increase safety; and\n**(ii)**\nestablish front seat crashworthiness side impact tests with those testing devices for adult female occupants in all designated front seating positions tested, as of the date of enactment of this Act, for adult male occupants.\n**(C) New car assessment program update**\n**(i) In general**\nThe Secretary shall promulgate a final decision notice to update the testing procedures used to test the crashworthiness of passenger motor vehicles under the New Car Assessment Program of the National Highway Traffic Safety Administration to require the use of the testing devices described in subparagraphs (A) and (B) of paragraph (1).\n**(ii) Timing**\n**(I) In general**\nThe final decision notice required under clause (i) shall be promulgated concurrently with the issuance of the final rule required under subparagraph (A)(ii) if the Secretary determines that promulgating the final decision notice concurrently with the final rule required under that subparagraph does not delay issuance of that final rule.\n**(II) Delay**\nIf the Secretary determines under subclause (I) that promulgating the final decision notice concurrently with the final rule required under subparagraph (A)(ii) would delay the issuance of that final rule, the Secretary shall issue that final rule before promulgating the final decision notice required under this subparagraph.\n#### 4. Testing devices roadmap\n##### (a) Initial report\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that\u2014\n**(A)**\nidentifies timelines for the Secretary to incorporate testing devices, other than the testing devices described in subparagraphs (A) and (B) of section 3(a)(1) and subparagraphs (A) and (B) of section 3(b)(1), that the Secretary is researching, as of the date of enactment of this Act, into the regulations contained in parts 571 and 572 of title 49, Code of Federal Regulations (or successor regulations);\n**(B)**\nidentifies testing devices used for similar crashworthiness standards in other countries that are more advanced than the testing devices required or being researched by the Secretary; and\n**(C)**\nsubject to paragraph (2), describes a process for the Secretary to update the testing devices required in the United States under regulations in effect on the date of enactment of this Act, including whether the Secretary can adopt more advanced testing devices already used for compliance in other countries, such as testing devices in use or being considered as part of the European New Car Assessment Programme.\n**(2) No update needed**\nIf the Secretary determines that testing devices used in the United States as of the date of enactment of this Act do not need to be updated, the Secretary shall include in the report required under paragraph (1) a description for why the Secretary believes those testing devices do not need to be updated, including by providing a description for each testing device described in part 572 of title 49, Code of Federal Regulations (or successor regulations), that the Secretary determines does not need to be updated.\n##### (b) Follow-Up report\nNot later than 5 years after the date on which the Secretary submits the report required under subsection (a), the Secretary shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that\u2014\n**(1)**\ndescribes whether the Secretary has met the timelines described in subsection (a)(1)(A); and\n**(2)**\nidentifies any new testing devices used in other countries that are more advanced than the testing devices required or being research by the Secretary as of the date of enactment of this Act.",
      "versionDate": "2025-01-31",
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
            "name": "Accidents",
            "updateDate": "2025-02-12T14:21:11Z"
          },
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-02-12T14:20:37Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-12T14:21:25Z"
          },
          {
            "name": "Department of Transportation",
            "updateDate": "2025-02-12T14:20:47Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-02-12T14:20:55Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-02-12T14:21:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-05T16:45:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-31",
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
          "measure-id": "id119s161",
          "measure-number": "161",
          "measure-type": "s",
          "orig-publish-date": "2025-07-31",
          "originChamber": "SENATE",
          "update-date": "2026-03-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s161v25",
            "update-date": "2026-03-12"
          },
          "action-date": "2025-07-31",
          "action-desc": "Reported to Senate",
          "summary-text": "<p><strong>She Develops Regulations In Vehicle Equality and Safety Act or the She DRIVES Act</strong></p><p>This bill directs the Department of Transportation (DOT) to revise motor vehicle\u00a0safety standards to require the use of certain anthropomorphic test devices (i.e., crash test dummies) and testing on female crash test dummies.</p><p>Specifically, DOT must issue final rules to revise the current testing regulations to include specific adult male and adult female frontal impact and side impact crash test dummies. </p><p>The final rules must establish or update the testing injury criteria based on real-world injuries and the greatest potential to increase safety. The injury criteria must include head, neck, chest, abdomen, pelvis,\u00a0upper leg, and lower leg criteria for the crash test dummies.</p><p>The final rules must also establish crashworthiness frontal and side impact tests for adult female occupants in all front seating positions that are currently tested for adult male occupants (as of the date of the bill's enactment).</p><p>Further, DOT must promulgate a final decision notice to update the testing procedures for the \u00a0New Car Assessment Program of the National Highway Traffic Safety Administration to require the use of these crash test dummies\u00a0for frontal and side impact\u00a0crashworthiness testing.</p><p>Finally, DOT must submit reports to Congress that, among other things, identify timelines for DOT to incorporate additional types of crash test dummies into the regulations and identify testing devices used in other countries for similar\u00a0crashworthiness standards.</p>"
        },
        "title": "She DRIVES Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s161.xml",
    "summary": {
      "actionDate": "2025-07-31",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>She Develops Regulations In Vehicle Equality and Safety Act or the She DRIVES Act</strong></p><p>This bill directs the Department of Transportation (DOT) to revise motor vehicle\u00a0safety standards to require the use of certain anthropomorphic test devices (i.e., crash test dummies) and testing on female crash test dummies.</p><p>Specifically, DOT must issue final rules to revise the current testing regulations to include specific adult male and adult female frontal impact and side impact crash test dummies. </p><p>The final rules must establish or update the testing injury criteria based on real-world injuries and the greatest potential to increase safety. The injury criteria must include head, neck, chest, abdomen, pelvis,\u00a0upper leg, and lower leg criteria for the crash test dummies.</p><p>The final rules must also establish crashworthiness frontal and side impact tests for adult female occupants in all front seating positions that are currently tested for adult male occupants (as of the date of the bill's enactment).</p><p>Further, DOT must promulgate a final decision notice to update the testing procedures for the \u00a0New Car Assessment Program of the National Highway Traffic Safety Administration to require the use of these crash test dummies\u00a0for frontal and side impact\u00a0crashworthiness testing.</p><p>Finally, DOT must submit reports to Congress that, among other things, identify timelines for DOT to incorporate additional types of crash test dummies into the regulations and identify testing devices used in other countries for similar\u00a0crashworthiness standards.</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119s161"
    },
    "title": "She DRIVES Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-31",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>She Develops Regulations In Vehicle Equality and Safety Act or the She DRIVES Act</strong></p><p>This bill directs the Department of Transportation (DOT) to revise motor vehicle\u00a0safety standards to require the use of certain anthropomorphic test devices (i.e., crash test dummies) and testing on female crash test dummies.</p><p>Specifically, DOT must issue final rules to revise the current testing regulations to include specific adult male and adult female frontal impact and side impact crash test dummies. </p><p>The final rules must establish or update the testing injury criteria based on real-world injuries and the greatest potential to increase safety. The injury criteria must include head, neck, chest, abdomen, pelvis,\u00a0upper leg, and lower leg criteria for the crash test dummies.</p><p>The final rules must also establish crashworthiness frontal and side impact tests for adult female occupants in all front seating positions that are currently tested for adult male occupants (as of the date of the bill's enactment).</p><p>Further, DOT must promulgate a final decision notice to update the testing procedures for the \u00a0New Car Assessment Program of the National Highway Traffic Safety Administration to require the use of these crash test dummies\u00a0for frontal and side impact\u00a0crashworthiness testing.</p><p>Finally, DOT must submit reports to Congress that, among other things, identify timelines for DOT to incorporate additional types of crash test dummies into the regulations and identify testing devices used in other countries for similar\u00a0crashworthiness standards.</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119s161"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s161is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s161rs.xml"
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
      "title": "She DRIVES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T12:03:18Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "She DRIVES Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-08-02T03:08:20Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "She Develops Regulations In Vehicle Equality and Safety Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-08-02T03:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "She DRIVES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "She Develops Regulations In Vehicle Equality and Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Transportation to issue rules relating to the testing procedures used under the New Car Assessment Program of the National Highway Traffic Safety Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T15:18:17Z"
    }
  ]
}
```
