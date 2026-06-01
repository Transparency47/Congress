# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1498?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1498
- Title: Halting Ownership and Non-Ethical Stock Transactions (HONEST) Act
- Congress: 119
- Bill type: S
- Bill number: 1498
- Origin chamber: Senate
- Introduced date: 2025-04-28
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-28: Introduced in Senate
- 2025-04-28 - IntroReferral: Introduced in Senate
- 2025-04-28 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-12-10 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-12-10 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-12-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 294.
- Latest action: 2025-04-28: Introduced in Senate

## Actions

- 2025-04-28 - IntroReferral: Introduced in Senate
- 2025-04-28 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-12-10 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-12-10 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-12-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 294.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1498",
    "number": "1498",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Halting Ownership and Non-Ethical Stock Transactions (HONEST) Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 294.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-12-10",
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
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-28",
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
      "actionDate": "2025-04-28",
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
            "date": "2025-12-10T22:36:31Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:00:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-28T21:02:50Z",
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
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "OH"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "GA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "OR"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1498is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1498\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2025 Mr. Hawley (for himself and Mr. Moreno ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend chapter 131 of title 5, United States Code, to prohibit transactions involving certain financial instruments by Members of Congress.\n#### 1. Short title\nThis Act may be cited as the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act .\n#### 2. Banning insider trading in Congress\n##### (a) In general\nChapter 131 of title 5, United States Code, is amended by adding at the end the following:\nIV Banning insider trading in Congress 13161. Definitions In this subchapter: (1) Covered financial instrument (A) In general The term covered financial instrument means\u2014 (i) any investment in\u2014 (I) a security (as defined in section 3(a) of Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (II) a security future (as defined in that section); or (III) a commodity (as defined in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a )); and (ii) any economic interest comparable to an interest described in clause (i) that is acquired through synthetic means, such as the use of a derivative, including an option, a warrant, or other similar means. (B) Exclusions The term covered financial instrument does not include\u2014 (i) a diversified mutual fund; (ii) a diversified exchange-traded fund; (iii) a United States Treasury bill, note, or bond; or (iv) compensation from the primary occupation of a spouse or dependent child of a Member of Congress. (2) Dependent child; Member of Congress The terms dependent child and Member of Congress have the meanings given those terms in section 13101. (3) Supervising ethics committee The term supervising ethics committee means, as applicable\u2014 (A) the Select Committee on Ethics of the Senate; and (B) the Committee on Ethics of the House of Representatives. 13162. Prohibition on certain transactions and holdings involving covered financial instruments (a) Prohibition Except as provided in subsection (b), a Member of Congress, or any spouse of a Member of Congress, may not, during the term of service of the Member of Congress, hold, purchase, or sell any covered financial instrument. (b) Exceptions The prohibition under subsection (a) shall not apply to a sale by a Member of Congress, or a spouse of a Member of Congress, that is completed by the date that is\u2014 (1) for a Member of Congress serving on the date of enactment of the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act , 180 days after that date of enactment; and (2) for any Member of Congress who commences service as a Member of Congress after the date of enactment of the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act , 180 days after the first date of the initial term of service. (c) Penalties (1) Disgorgement A Member of Congress shall disgorge to the Treasury of the United States any profit from a transaction or holding involving a covered financial instrument that is conducted in violation of this section. (2) Fines A Member of Congress who holds or conducts a transaction involving, or whose spouse holds or conducts a transaction involving, a covered financial instrument in violation of this section may be subject to a civil fine assessed by the applicable supervising ethics committee under section 13164. 13163. Certification of compliance (a) In general Not less frequently than annually, each Member of Congress shall submit to the applicable supervising ethics committee a written certification that the Member of Congress has achieved compliance with the requirements of this subchapter. (b) Publication The supervising ethics committees shall publish each certification submitted under subsection (a) on a publicly available website. 13164. Authority of supervising ethics committees (a) In general The supervising ethics committees may implement and enforce the requirements of this subchapter, including by\u2014 (1) issuing\u2014 (A) for Members of Congress\u2014 (i) rules governing that implementation; and (ii) 1 or more reasonable extensions to achieve compliance with this subchapter, if the applicable supervising ethics committee determines that a Member of Congress is making a good faith effort to divest any covered financial instruments; and (B) guidance relating to covered financial instruments; (2) publishing on the internet certifications submitted by Members of Congress under section 13163(a); and (3) assessing civil fines against any Member of Congress who is in violation of this subchapter, subject to subsection (b). (b) Requirements for civil fines (1) In general Before imposing a fine pursuant to this section, the applicable supervising ethics committee shall provide to the applicable Member of Congress\u2014 (A) a written notice describing each covered financial instrument transaction for which a fine will be assessed; and (B) an opportunity, with respect to each such covered financial instrument transaction\u2014 (i) for a hearing; and (ii) to achieve compliance with the requirements of this subchapter. (2) Enforcement (A) In general In the event of continuing noncompliance after issuance of the notice described in paragraph (1), the applicable supervising ethics committee shall impose a civil penalty, in the amount described in subparagraph (B), on the Member of Congress to whom a notice was provided\u2014 (i) on the date that is 30 days after the date of provision of the notice; and (ii) during the period in which such noncompliance continues, not less frequently than once every 30 days thereafter. (B) Amount The amount of each civil penalty imposed on a Member of Congress pursuant to subparagraph (A) shall be an amount equal to 10 percent of the value of each covered financial instrument that was not divested in violation of this subchapter during the period covered by the penalty. (3) Publication Each supervising ethics committee shall publish on a publicly available website a description of\u2014 (A) each fine assessed by the supervising ethics committee pursuant to this section; (B) the reasons why each such fine was assessed; and (C) the result of each assessment, including any hearing under paragraph (1)(B)(i) relating to the assessment. (4) Appeal A Member of Congress may appeal the assessment of a fine under this section to a vote on the floor of the Senate or the House of Representatives, as applicable, as a privileged motion. 13165. Audit by Government Accountability Office Not later than 2 years after the date of enactment of the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act , the Comptroller General of the United States shall\u2014 (1) conduct an audit of the compliance by Members of Congress with the requirements of this subchapter; and (2) submit to the supervising ethics committees a report describing the results of the audit conducted under paragraph (1). .\n##### (b) Conforming amendments\n**(1) Table of sections**\nThe table of sections for chapter 131 of title 5, United States Code, is amended by adding at the end the following:\nSUBCHAPTER IV\u2014Banning insider trading in Congress 13161. Definitions. 13162. Prohibition on certain transactions and holdings involving covered financial instruments. 13163. Certification of compliance. 13164. Authority of supervising ethics committees. 13165. Audit by Government Accountability Office. .\n**(2) Persons required to file**\nSection 13103(f) of title 5, United States Code, is amended\u2014\n**(A)**\nin paragraph (9), by striking \u201cas defined in section 13101 of this title\u201d;\n**(B)**\nin paragraph (10), by striking \u201cas defined in section 13101 of this title\u201d;\n**(C)**\nin paragraph (11), by striking \u201cas defined in section 13101 of this title\u201d; and\n**(D)**\nin paragraph (12), by striking \u201cas defined in section 13101 of this title\u201d.\n**(3) Lobbying Disclosure Act of 1995**\nSection 3(4)(D) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602(4)(D) ) is amended by striking legislative branch employee serving in a position described under section 13101(13) of title 5, United States Code and inserting officer or employee of Congress (as defined in section 13101 of title 5, United States Code) .",
      "versionDate": "2025-04-28",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1498rs.xml",
      "text": "II\nCalendar No. 294\n119th CONGRESS\n1st Session\nS. 1498\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2025 Mr. Hawley (for himself, Mr. Moreno , Mr. Ossoff , Mr. Peters , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nDecember 10, 2025 Reported by Mr. Paul , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend chapter 131 of title 5, United States Code, to prohibit transactions involving certain financial instruments by Members of Congress.\n#### 1. Short title\nThis Act may be cited as the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act .\n#### 2. Banning insider trading in Congress\n##### (a) In general\nChapter 131 of title 5, United States Code, is amended by adding at the end the following:\nIV Banning insider trading in Congress 13161. Definitions In this subchapter: (1) Covered financial instrument (A) In general The term covered financial instrument means\u2014 (i) any investment in\u2014 (I) a security (as defined in section 3(a) of Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (II) a security future (as defined in that section); or (III) a commodity (as defined in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a )); and (ii) any economic interest comparable to an interest described in clause (i) that is acquired through synthetic means, such as the use of a derivative, including an option, a warrant, or other similar means. (B) Exclusions The term covered financial instrument does not include\u2014 (i) a diversified mutual fund; (ii) a diversified exchange-traded fund; (iii) a United States Treasury bill, note, or bond; or (iv) compensation from the primary occupation of a spouse or dependent child of a Member of Congress. (2) Dependent child; Member of Congress The terms dependent child and Member of Congress have the meanings given those terms in section 13101. (3) Supervising ethics committee The term supervising ethics committee means, as applicable\u2014 (A) the Select Committee on Ethics of the Senate; and (B) the Committee on Ethics of the House of Representatives. 13162. Prohibition on certain transactions and holdings involving covered financial instruments (a) Prohibition Except as provided in subsection (b), a Member of Congress, or any spouse of a Member of Congress, may not, during the term of service of the Member of Congress, hold, purchase, or sell any covered financial instrument. (b) Exceptions The prohibition under subsection (a) shall not apply to a sale by a Member of Congress, or a spouse of a Member of Congress, that is completed by the date that is\u2014 (1) for a Member of Congress serving on the date of enactment of the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act , 180 days after that date of enactment; and (2) for any Member of Congress who commences service as a Member of Congress after the date of enactment of the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act , 180 days after the first date of the initial term of service. (c) Penalties (1) Disgorgement A Member of Congress shall disgorge to the Treasury of the United States any profit from a transaction or holding involving a covered financial instrument that is conducted in violation of this section. (2) Fines A Member of Congress who holds or conducts a transaction involving, or whose spouse holds or conducts a transaction involving, a covered financial instrument in violation of this section may be subject to a civil fine assessed by the applicable supervising ethics committee under section 13164. 13163. Certification of compliance (a) In general Not less frequently than annually, each Member of Congress shall submit to the applicable supervising ethics committee a written certification that the Member of Congress has achieved compliance with the requirements of this subchapter. (b) Publication The supervising ethics committees shall publish each certification submitted under subsection (a) on a publicly available website. 13164. Authority of supervising ethics committees (a) In general The supervising ethics committees may implement and enforce the requirements of this subchapter, including by\u2014 (1) issuing\u2014 (A) for Members of Congress\u2014 (i) rules governing that implementation; and (ii) 1 or more reasonable extensions to achieve compliance with this subchapter, if the applicable supervising ethics committee determines that a Member of Congress is making a good faith effort to divest any covered financial instruments; and (B) guidance relating to covered financial instruments; (2) publishing on the internet certifications submitted by Members of Congress under section 13163(a); and (3) assessing civil fines against any Member of Congress who is in violation of this subchapter, subject to subsection (b). (b) Requirements for civil fines (1) In general Before imposing a fine pursuant to this section, the applicable supervising ethics committee shall provide to the applicable Member of Congress\u2014 (A) a written notice describing each covered financial instrument transaction for which a fine will be assessed; and (B) an opportunity, with respect to each such covered financial instrument transaction\u2014 (i) for a hearing; and (ii) to achieve compliance with the requirements of this subchapter. (2) Enforcement (A) In general In the event of continuing noncompliance after issuance of the notice described in paragraph (1), the applicable supervising ethics committee shall impose a civil penalty, in the amount described in subparagraph (B), on the Member of Congress to whom a notice was provided\u2014 (i) on the date that is 30 days after the date of provision of the notice; and (ii) during the period in which such noncompliance continues, not less frequently than once every 30 days thereafter. (B) Amount The amount of each civil penalty imposed on a Member of Congress pursuant to subparagraph (A) shall be an amount equal to 10 percent of the value of each covered financial instrument that was not divested in violation of this subchapter during the period covered by the penalty. (3) Publication Each supervising ethics committee shall publish on a publicly available website a description of\u2014 (A) each fine assessed by the supervising ethics committee pursuant to this section; (B) the reasons why each such fine was assessed; and (C) the result of each assessment, including any hearing under paragraph (1)(B)(i) relating to the assessment. (4) Appeal A Member of Congress may appeal the assessment of a fine under this section to a vote on the floor of the Senate or the House of Representatives, as applicable, as a privileged motion. 13165. Audit by Government Accountability Office Not later than 2 years after the date of enactment of the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act , the Comptroller General of the United States shall\u2014 (1) conduct an audit of the compliance by Members of Congress with the requirements of this subchapter; and (2) submit to the supervising ethics committees a report describing the results of the audit conducted under paragraph (1). .\n##### (b) Conforming amendments\n**(1) Table of sections**\nThe table of sections for chapter 131 of title 5, United States Code, is amended by adding at the end the following:\nSUBCHAPTER IV\u2014Banning insider trading in Congress 13161. Definitions. 13162. Prohibition on certain transactions and holdings involving covered financial instruments. 13163. Certification of compliance. 13164. Authority of supervising ethics committees. 13165. Audit by Government Accountability Office. .\n**(2) Persons required to file**\nSection 13103(f) of title 5, United States Code, is amended\u2014\n**(A)**\nin paragraph (9), by striking \u201cas defined in section 13101 of this title\u201d;\n**(B)**\nin paragraph (10), by striking \u201cas defined in section 13101 of this title\u201d;\n**(C)**\nin paragraph (11), by striking \u201cas defined in section 13101 of this title\u201d; and\n**(D)**\nin paragraph (12), by striking \u201cas defined in section 13101 of this title\u201d.\n**(3) Lobbying Disclosure Act of 1995**\nSection 3(4)(D) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602(4)(D) ) is amended by striking legislative branch employee serving in a position described under section 13101(13) of title 5, United States Code and inserting officer or employee of Congress (as defined in section 13101 of title 5, United States Code) .",
      "versionDate": "2025-12-10",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-08-26T14:35:18Z"
          },
          {
            "name": "Commodities markets",
            "updateDate": "2025-08-26T14:35:52Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-26T14:35:36Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-08-26T14:36:08Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-08-26T14:36:01Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-08-26T14:35:43Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-26T14:36:15Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-08-26T14:35:30Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-08-26T14:35:03Z"
          },
          {
            "name": "Securities",
            "updateDate": "2025-08-26T14:35:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-08T18:06:38Z"
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
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1498is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1498rs.xml"
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
      "title": "Halting Ownership and Non-Ethical Stock Transactions (HONEST) Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Halting Ownership and Non-Ethical Stock Transactions (HONEST) Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-12-12T03:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-08T04:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 131 of title 5, United States Code, to prohibit transactions involving certain financial instruments by Members of Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T04:33:31Z"
    }
  ]
}
```
