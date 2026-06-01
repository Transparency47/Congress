# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4107
- Title: Antitrust Accountability and Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 4107
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-04-02T19:03:16Z
- Update date including text: 2026-04-02T19:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-17: Introduced in Senate

## Actions

- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4107",
    "number": "4107",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
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
    "title": "Antitrust Accountability and Transparency Act",
    "type": "S",
    "updateDate": "2026-04-02T19:03:16Z",
    "updateDateIncludingText": "2026-04-02T19:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
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
      "actionDate": "2026-03-17",
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
        "item": {
          "date": "2026-03-17T15:41:24Z",
          "name": "Referred To"
        }
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NJ"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "MA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4107is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4107\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Ms. Klobuchar (for herself, Mr. Durbin , Mr. Booker , Ms. Hirono , Mr. Blumenthal , Mr. Welch , Ms. Warren , Mr. Murphy , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 5 of the Clayton Act to include proposed voluntary dismissals in the court's consideration of proposed consent judgments and clarify the public interest, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Antitrust Accountability and Transparency Act .\n#### 2. Amendments\nSection 5 of the Clayton Act ( 15 U.S.C. 16 ) is amended\u2014\n**(1)**\nin subsection (a), by striking or under section 5 of the Federal Trade Commission Act which could give rise to a claim for relief under the antitrust laws ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby inserting or administrative after any civil ;\n**(ii)**\nby inserting , or in the case of an administrative proceeding, a district court in which 1 or more defendants is incorporated or headquartered, after the district court before which such proceeding is pending ;\n**(iii)**\nby striking published by the United States and inserting published each place it appears;\n**(iv)**\nby striking 60 days and inserting 45 days ;\n**(v)**\nby inserting A district court to which a consent judgment is submitted by the Federal Trade Commission in compliance with this subsection is invested with jurisdiction under this section. after prior to the effective date of such judgment. ; and\n**(vi)**\nby striking sixty-day period and inserting 45-day period ;\n**(B)**\nin paragraph (3), by inserting any commitments made by the parties to the United States or Federal Trade Commission not memorialized in the proposal related to the proceeding, how the proposal remedies any material risk that the antitrust laws may be violated, after thereby, ; and\n**(C)**\nin paragraph (6), by inserting or Federal Trade Commission, including any settlement offers, divestitures, or other remedies, including the process through which these proposals were considered before the period;\n**(3)**\nin subsection (c) by striking 60 days and inserting 45 days ;\n**(4)**\nin subsection (d)\u2014\n**(A)**\nby striking during the 60-day period and inserting the following: (1) during the 45-day period ;\n**(B)**\nin paragraph (1), as so designated\u2014\n**(i)**\nby striking his designee and inserting a designee thereof ;\n**(ii)**\nby striking such 60-day time period and inserting such 45-day time period ;\n**(iii)**\nby striking At the close of and inserting Not later than 30 days after the close of ;\n**(iv)**\nby inserting Parties that submitted comments shall be allowed to submit a reply to the responses published by the United States or Federal Trade Commission. before the last sentence; and\n**(v)**\nby adding at the end Compliance with this section by the Federal Trade Commission shall satisfy any other notice-and-comment requirements relating to consent judgments. ; and\n**(C)**\nby adding at the end the following:\n(2) (A) In a proceeding brought under section 7, the parties shall continue to hold all assets related to the transaction separate as if they are subject to a waiting period under section 7A until the date that is 15 days after the United States or Federal Trade Commission files with the district court and causes to be published in the Federal Register a response to comments under this subsection. The court may extend the period during which the parties are required to hold all assets related to the transaction separate upon a finding that\u2014 (i) there is a reasonable likelihood that the court will determine that the consent judgment does not meet the requirements in subsection (e)(1); and (ii) the balance of the equities favors extending the order. (B) In the event that the court extends the period during which the parties are required to hold all assets separate, the court shall make all reasonable efforts to expedite its determination under subsection (e)(1). (3) A violation of paragraph (2) shall be treated as a violation of section 7A and parties may be liable for civil penalties pursuant to subsection (g) of that section. (4) Any order to hold assets separate shall expire upon a finding by the court that the consent judgment satisfies the requirements under subsection (e)(1). .\n**(5)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting there is a reasonable belief, based on evidence and reasoned analysis, that after the court shall determine that ; and\n**(ii)**\nin subparagraph (A), by inserting , does not permit any transaction, merger, agreement, business practice, or other course of conduct that creates a material risk of violating the antitrust laws, and that the provisions of the consent judgment are reasonably tailored to the violations of the antitrust laws alleged in the complaint after whether the consent judgment is in the public interest ;\n**(B)**\nin paragraph (2), by striking or to require the court to permit anyone to intervene and inserting , but the court shall take into account any written request for a hearing by any Federal or State agency, including any State attorney general, when determining whether to conduct an evidentiary hearing ; and\n**(C)**\nby adding at the end the following:\n(3) If the court determines that an evidentiary hearing is appropriate, any Federal or State agency, including any State attorney general that made a written request under paragraph (2), shall be allowed to intervene. Nothing shall require the court to permit any other party to intervene. (4) A consent judgment filed under this section shall take effect only upon entry by the court. The decision to enter a consent judgment under this section is within the discretion of the court, which need not defer to the United States\u2019s predictions about the efficacy of its remedies. ;\n**(6)**\nin subsection (f)\u2014\n**(A)**\nby inserting current or former before Government officials ;\n**(B)**\nin paragraph (4), by striking and at the end;\n**(C)**\nby redesignating paragraph (5) as paragraph (7); and\n**(D)**\nby inserting after paragraph (4) the following:\n(5) order the production of the communications that were disclosed or should have been disclosed pursuant to subsection (g), including all related documents and testimony relating to the communications; (6) order the production of information or testimony regarding the provision of, or offer to provide, a benefit or concession by any party in the proceeding to the Government or an employee or officer thereof, including payments, donations, or alterations in policy or business practices that the court finds may have a reasonable connection to the proceeding or decision to enter the proposed judgment; and ;\n**(7)**\nin subsection (g)\u2014\n**(A)**\nby inserting , including the Executive Office of the President, after any officer or employee of the United States ; and\n**(B)**\nby striking except that any and inserting , and shall include the date of each written or oral communication and each author of, recipient of, and participant to each written or oral communication. Any ;\n**(8)**\nin subsection (h), by inserting , or by the Federal Trade Commission under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), after under section 4A of this Act ; and\n**(9)**\nby adding at the end the following:\n(j) Voluntary dismissals (1) In general Any proposal to file a motion to voluntarily dismiss any civil proceeding brought by the United States or Federal Trade Commission under the antitrust laws shall be filed with the district court before which such proceeding is pending, and published in the Federal Register not less than 45 days prior to the effective date of such voluntary dismissal. The case shall be stayed during this 45-day period. (2) Substitution During the 45-day period under paragraph (1), any State attorney general may file a motion for substitution in the proceeding. A court shall grant the motion for substitution unless presented with clear and convincing evidence by the parties that there are no genuine issues of material fact that could support any claim in the proceeding or that the defendant would be entitled to judgment as a matter of law. If the motion for substitution is granted, the action does not abate, but proceeds in favor of or against the remaining parties. (3) Transfer Upon a grant of a motion for substitution under paragraph (2), the United States or the Federal Trade Commission shall promptly transfer all materials relevant to the litigation that are not subject to the deliberative process privilege to the applicable State attorneys general and the case shall continue on a schedule that will not cause undue delay, as determined appropriate by the court. (k) References In this section, all references to\u2014 (1) the United States or the Attorney General shall be deemed to include the Federal Trade Commission, as applicable; and (2) the antitrust laws shall be deemed to include an unfair method of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ). .",
      "versionDate": "2026-03-17",
      "versionType": "Introduced in Senate"
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
        "name": "Commerce",
        "updateDate": "2026-04-02T19:03:15Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4107is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Antitrust Accountability and Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Antitrust Accountability and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 5 of the Clayton Act to include proposed voluntary dismissals in the court's consideration of proposed consent judgements and clarify the public interest, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T04:18:41Z"
    }
  ]
}
```
