# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/233?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/233
- Title: Restoring Confidence in the World Anti-Doping Agency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 233
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-03-03T21:26:20Z
- Update date including text: 2026-03-03T21:26:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-06-25 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-23 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-111.
- 2026-02-23 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-111.
- 2026-02-23 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 340.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-06-25 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-23 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-111.
- 2026-02-23 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-111.
- 2026-02-23 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 340.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/233",
    "number": "233",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Restoring Confidence in the World Anti-Doping Agency Act of 2025",
    "type": "S",
    "updateDate": "2026-03-03T21:26:20Z",
    "updateDateIncludingText": "2026-03-03T21:26:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 340.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-02-23",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-111.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-02-23",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-111.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
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
            "date": "2026-02-23T20:31:51Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-25T14:38:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-23T21:37:08Z",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MD"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WV"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "DE"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s233is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 233\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mrs. Blackburn (for herself, Mr. Van Hollen , Mrs. Capito , Mr. Blumenthal , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Office of National Drug Control Policy Reauthorization Act of 2006 to modify the authority of the Office of National Drug Control Policy with respect to the World Anti-Doping Agency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring Confidence in the World Anti-Doping Agency Act of 2025 .\n#### 2. Authority of National Drug Control Policy with respect to the World Anti-Doping Agency\nSection 701 of the Office of National Drug Control Policy Reauthorization Act of 2006 ( 21 U.S.C. 2001 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) United States Olympic and Paralympic Committee The term United States Olympic and Paralympic Committee means the organization established by chapter 2205 of title 36, United States Code. ;\n**(B)**\nin paragraph (3), by striking ( 36 U.S.C. 22501(b)(1) ) and inserting ( 36 U.S.C. 220501(b)(1) ) ;\n**(C)**\nby redesignating paragraphs (1) and (3) as paragraphs (4) and (1), respectively, and moving the paragraphs so as to appear in numeric order; and\n**(D)**\nby inserting after paragraph (2) the following:\n(3) Independent athlete The term independent athlete means an Olympic or Paralympic athlete who does not serve, in any capacity\u2014 (A) on the International Olympic Committee; (B) on the International Paralympic Committee; (C) at an international sports federation recognized by the International Olympic Committee or the International Paralympic Committee; (D) on the United States Olympic and Paralympic Committee; or (E) at the World Anti-Doping Agency. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking United States Olympic Committee each place it appears and inserting United States Olympic and Paralympic Committee ;\n**(B)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(6) carry out responsibilities with respect to the World Anti-Doping Agency, as described in subsection (d). ; and\n**(3)**\nby adding at the end the following:\n(d) Authority with respect to the World Anti-Doping Agency (1) In general The Office of National Drug Control Policy, in consultation with the United States Anti-Doping Agency, the United States Olympic and Paralympic Committee, and the Team USA Athletes\u2019 Commission, shall\u2014 (A) use all available tools to ensure that\u2014 (i) the World Anti-Doping Agency has a credible and independent governance model that provides for fair representation of the United States; (ii) the World Anti-Doping Agency fully implements all governance reforms, including a proper conflict-of-interest policy for all members of the Executive Committee, the Foundation Board, and all relevant expert advisory groups, standing committees, permanent special committees, and working groups of the World Anti-Doping Agency; and (iii) independent athletes from the United States and other democratic countries, or representatives of such athletes, have decision-making roles on the Executive Committee and the Foundation Board, and in all relevant expert advisory groups, standing committees, permanent special committees, and working groups, of the World Anti-Doping Agency; (B) demonstrate leadership within the global community; (C) have strict standards that work toward countering doping in every form, including by countering systemic fraud through doping involving\u2014 (i) governmental law enforcement, intelligence, or anti-doping institutions; (ii) sporting organizations; or (iii) athlete support personnel; and (D) work collaboratively with democratic countries. (2) Determination (A) In general Not later than 90 days after the date of the enactment of this subsection, the Office of National Drug Control Policy, in consultation with the United States Anti-Doping Agency, the United States Olympic and Paralympic Committee, and the Team USA Athletes\u2019 Commission, shall make a determination as to whether the World Anti-Doping Agency\u2014 (i) has a credible and independent governance model that provides for fair representation of the United States; (ii) fully implements all governance reforms, including a proper conflict-of-interest policy described in paragraph (1)(A)(ii); and (iii) allows independent athletes from the United States and other democratic countries, or representatives of such athletes, to have decision-making roles on the Executive Committee and the Foundation Board, and in all relevant expert advisory groups, standing committees, permanent special committees, and working groups, of the World Anti-Doping Agency. (B) Accountability In the case of a determination under subparagraph (A) that the World Anti-Doping Agency does not have such a governance model, has not fully implemented such governance reforms, or has not allowed decision-making roles described in clause (iii) of that subparagraph, the Office of National Drug Control Policy, in consultation with the United States Anti-Doping Agency, the United States Olympic and Paralympic Committee, and the Team USA Athletes\u2019 Commission, shall\u2014 (i) use all available tools to ensure that the United States has fair representation in the World Anti-Doping Agency, including\u2014 (I) on the Executive Committee; (II) on the Foundation Board; and (III) in all relevant expert advisory groups, standing committees, permanent special committees, and working groups of the World Anti-Doping Agency; and (ii) not later than 180 days after the date on which the determination under subparagraph (A) is made, issue a report that describes the barriers to participation and fair representation of the United States on the Executive Committee, the Foundation Board, and all relevant expert advisory groups, standing committees, permanent special committees, and working groups of the World Anti-Doping Agency. (3) Voluntary nonpayment of dues (A) In general In the case of a determination under paragraph (2)(A) that the World Anti-Doping Agency does not have a governance model that provides for fair representation of the United States, has not fully implemented governance reforms, or has not allowed decision-making roles described in clause (iii) of that subparagraph, the Office of National Drug Control Policy, in consultation with the appropriate committees of Congress, may voluntarily withhold up to the full amount of membership dues to the World Anti-Doping Agency. (B) Appropriate committees of Congress defined In this paragraph, the term appropriate committees of Congress means\u2014 (i) the Subcommittee on Consumer Protection, Product Safety, and Data Security of the Committee on Commerce, Science, and Transportation of the Senate (or a successor subcommittee); (ii) the Subcommittee on Financial Services and General Government of the Committee on Appropriations of the Senate (or a successor subcommittee); (iii) the Subcommittee on Oversight and Investigations of the Committee on Energy and Commerce of the House of Representatives (or a successor subcommittee); and (iv) the Subcommittee on Financial Services and General Government of the Committee on Appropriations of the House of Representatives (or a successor subcommittee). (4) Spending plan Not later than 30 days before the Office of National Drug Control Policy obligates funds to the World Anti-Doping Agency, the Office of National Drug Control Policy shall submit to the Committee on Appropriations of the Senate and the Committee on Appropriations of the House of Representatives a spending plan and explanation of proposed uses of such funds. .",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s233rs.xml",
      "text": "II\nCalendar No. 340\n119th CONGRESS\n2d Session\nS. 233\n[Report No. 119\u2013111]\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mrs. Blackburn (for herself, Mr. Van Hollen , Mrs. Capito , Mr. Blumenthal , Mr. Wicker , Ms. Blunt Rochester , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nFebruary 23, 2026 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend the Office of National Drug Control Policy Reauthorization Act of 2006 to modify the authority of the Office of National Drug Control Policy with respect to the World Anti-Doping Agency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring Confidence in the World Anti-Doping Agency Act of 2025 .\n#### 2. Authority of National Drug Control Policy with respect to the World Anti-Doping Agency\nSection 701 of the Office of National Drug Control Policy Reauthorization Act of 2006 ( 21 U.S.C. 2001 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) United States Olympic and Paralympic Committee The term United States Olympic and Paralympic Committee means the organization established by chapter 2205 of title 36, United States Code. ;\n**(B)**\nin paragraph (3), by striking ( 36 U.S.C. 22501(b)(1) ) and inserting ( 36 U.S.C. 220501(b)(1) ) ;\n**(C)**\nby redesignating paragraphs (1) and (3) as paragraphs (4) and (1), respectively, and moving the paragraphs so as to appear in numeric order; and\n**(D)**\nby inserting after paragraph (2) the following:\n(3) Independent athlete The term independent athlete means an Olympic or Paralympic athlete who does not serve, in any capacity\u2014 (A) on the International Olympic Committee; (B) on the International Paralympic Committee; (C) at an international sports federation recognized by the International Olympic Committee or the International Paralympic Committee; (D) on the United States Olympic and Paralympic Committee; or (E) at the World Anti-Doping Agency. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking United States Olympic Committee each place it appears and inserting United States Olympic and Paralympic Committee ;\n**(B)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(6) carry out responsibilities with respect to the World Anti-Doping Agency, as described in subsection (d). ; and\n**(3)**\nby adding at the end the following:\n(d) Authority with respect to the World Anti-Doping Agency (1) In general The Office of National Drug Control Policy, in consultation with the United States Anti-Doping Agency, the United States Olympic and Paralympic Committee, and the Team USA Athletes\u2019 Commission, shall\u2014 (A) use all available tools to ensure that\u2014 (i) the World Anti-Doping Agency has a credible and independent governance model that provides for fair representation of the United States; (ii) the World Anti-Doping Agency fully implements all governance reforms, including a proper conflict-of-interest policy for all members of the Executive Committee, the Foundation Board, and all relevant expert advisory groups, standing committees, permanent special committees, and working groups of the World Anti-Doping Agency; and (iii) independent athletes from the United States and other democratic countries, or representatives of such athletes, have decision-making roles on the Executive Committee and the Foundation Board, and in all relevant expert advisory groups, standing committees, permanent special committees, and working groups, of the World Anti-Doping Agency; (B) demonstrate leadership within the global community; (C) have strict standards that work toward countering doping in every form, including by countering systemic fraud through doping involving\u2014 (i) governmental law enforcement, intelligence, or anti-doping institutions; (ii) sporting organizations; or (iii) athlete support personnel; and (D) work collaboratively with democratic countries. (2) Determination (A) In general Not later than 90 days after the date of the enactment of this subsection, the Office of National Drug Control Policy, in consultation with the United States Anti-Doping Agency, the United States Olympic and Paralympic Committee, and the Team USA Athletes\u2019 Commission, shall make a determination as to whether the World Anti-Doping Agency\u2014 (i) has a credible and independent governance model that provides for fair representation of the United States; (ii) fully implements all governance reforms, including a proper conflict-of-interest policy described in paragraph (1)(A)(ii); and (iii) allows independent athletes from the United States and other democratic countries, or representatives of such athletes, to have decision-making roles on the Executive Committee and the Foundation Board, and in all relevant expert advisory groups, standing committees, permanent special committees, and working groups, of the World Anti-Doping Agency. (B) Accountability In the case of a determination under subparagraph (A) that the World Anti-Doping Agency does not have such a governance model, has not fully implemented such governance reforms, or has not allowed decision-making roles described in clause (iii) of that subparagraph, the Office of National Drug Control Policy, in consultation with the United States Anti-Doping Agency, the United States Olympic and Paralympic Committee, and the Team USA Athletes\u2019 Commission, shall\u2014 (i) use all available tools to ensure that the United States has fair representation in the World Anti-Doping Agency, including\u2014 (I) on the Executive Committee; (II) on the Foundation Board; and (III) in all relevant expert advisory groups, standing committees, permanent special committees, and working groups of the World Anti-Doping Agency; and (ii) not later than 180 days after the date on which the determination under subparagraph (A) is made, issue a report that describes the barriers to participation and fair representation of the United States on the Executive Committee, the Foundation Board, and all relevant expert advisory groups, standing committees, permanent special committees, and working groups of the World Anti-Doping Agency. (3) Voluntary nonpayment of dues (A) In general In the case of a determination under paragraph (2)(A) that the World Anti-Doping Agency does not have a governance model that provides for fair representation of the United States, has not fully implemented governance reforms, or has not allowed decision-making roles described in clause (iii) of that subparagraph, the Office of National Drug Control Policy, in consultation with the appropriate committees of Congress, may voluntarily withhold up to the full amount of membership dues to the World Anti-Doping Agency. (B) Appropriate committees of Congress defined In this paragraph, the term appropriate committees of Congress means\u2014 (i) the Subcommittee on Consumer Protection, Product Safety, and Data Security of the Committee on Commerce, Science, and Transportation of the Senate (or a successor subcommittee); (ii) the Subcommittee on Financial Services and General Government of the Committee on Appropriations of the Senate (or a successor subcommittee); (iii) the Subcommittee on Oversight and Investigations of the Committee on Energy and Commerce of the House of Representatives (or a successor subcommittee); and (iv) the Subcommittee on Financial Services and General Government of the Committee on Appropriations of the House of Representatives (or a successor subcommittee). (4) Spending plan Not later than 30 days before the Office of National Drug Control Policy obligates funds to the World Anti-Doping Agency, the Office of National Drug Control Policy shall submit to the Committee on Appropriations of the Senate and the Committee on Appropriations of the House of Representatives a spending plan and explanation of proposed uses of such funds. .",
      "versionDate": "2025-02-23",
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
        "actionDate": "2025-01-23",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "693",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Restoring Confidence in the World Anti-Doping Agency Act of 2025",
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
            "name": "Advisory bodies",
            "updateDate": "2025-08-29T15:57:43Z"
          },
          {
            "name": "Athletes",
            "updateDate": "2025-08-29T15:55:54Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-08-29T15:55:30Z"
          },
          {
            "name": "Olympic games",
            "updateDate": "2025-08-29T15:56:01Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-08-29T15:56:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Sports and Recreation",
        "updateDate": "2025-02-25T19:46:31Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s233is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-02-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s233rs.xml"
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
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Restoring Confidence in the World Anti-Doping Agency Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-26T07:53:29Z"
    },
    {
      "title": "Restoring Confidence in the World Anti-Doping Agency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Confidence in the World Anti-Doping Agency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Office of National Drug Control Policy Reauthorization Act of 2006 to modify the authority of the Office of National Drug Control Policy with respect to the World Anti-Doping Agency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:33:45Z"
    }
  ]
}
```
