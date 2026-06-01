# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3388?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3388
- Title: Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act
- Congress: 119
- Bill type: HR
- Bill number: 3388
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2025-12-05T21:58:00Z
- Update date including text: 2025-12-05T21:58:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-05-14 - IntroReferral: Sponsor introductory remarks on measure. (CR H2041-2042)
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-05-14 - IntroReferral: Sponsor introductory remarks on measure. (CR H2041-2042)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3388",
    "number": "3388",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "A000379",
        "district": "4",
        "firstName": "Mark",
        "fullName": "Rep. Alford, Mark [R-MO-4]",
        "lastName": "Alford",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:58:00Z",
    "updateDateIncludingText": "2025-12-05T21:58:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2041-2042)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3388ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3388\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Alford introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend chapter 131 of title 5, United States Code, to prohibit transactions involving certain financial instruments by Members of Congress.\n#### 1. Short title\nThis Act may be cited as the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act .\n#### 2. Banning insider trading in Congress\n##### (a) In general\nChapter 131 of title 5, United States Code, is amended by adding at the end the following:\nIV Banning insider trading in Congress 13161. Definitions In this subchapter: (1) Covered financial instrument (A) In general The term covered financial instrument means\u2014 (i) any investment in\u2014 (I) a security (as defined in section 3(a) of Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (II) a security future (as defined in that section); or (III) a commodity (as defined in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a )); and (ii) any economic interest comparable to an interest described in clause (i) that is acquired through synthetic means, such as the use of a derivative, including an option, a warrant, or other similar means. (B) Exclusions The term covered financial instrument does not include\u2014 (i) a diversified mutual fund; (ii) a diversified exchange-traded fund; (iii) a United States Treasury bill, note, or bond; or (iv) compensation from the primary occupation of a spouse or dependent child of a Member of Congress. (2) Dependent child; Member of Congress The terms dependent child and Member of Congress have the meanings given those terms in section 13101. (3) Supervising ethics committee The term supervising ethics committee means, as applicable\u2014 (A) the Select Committee on Ethics of the Senate; and (B) the Committee on Ethics of the House of Representatives. 13162. Prohibition on certain transactions and holdings involving covered financial instruments (a) Prohibition Except as provided in subsection (b), a Member of Congress, or any spouse of a Member of Congress, may not, during the term of service of the Member of Congress, hold, purchase, or sell any covered financial instrument. (b) Exceptions The prohibition under subsection (a) shall not apply to a sale by a Member of Congress, or a spouse of a Member of Congress, that is completed by the date that is\u2014 (1) for a Member of Congress serving on the date of enactment of the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act , 180 days after that date of enactment; and (2) for any Member of Congress who commences service as a Member of Congress after the date of enactment of the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act , 180 days after the first date of the initial term of service. (c) Penalties (1) Disgorgement A Member of Congress shall disgorge to the Treasury of the United States any profit from a transaction or holding involving a covered financial instrument that is conducted in violation of this section. (2) Fines A Member of Congress who holds or conducts a transaction involving, or whose spouse holds or conducts a transaction involving, a covered financial instrument in violation of this section may be subject to a civil fine assessed by the applicable supervising ethics committee under section 13164. 13163. Certification of compliance (a) In general Not less frequently than annually, each Member of Congress shall submit to the applicable supervising ethics committee a written certification that the Member of Congress has achieved compliance with the requirements of this subchapter. (b) Publication The supervising ethics committees shall publish each certification submitted under subsection (a) on a publicly available website. 13164. Authority of supervising ethics committees (a) In general The supervising ethics committees may implement and enforce the requirements of this subchapter, including by\u2014 (1) issuing\u2014 (A) for Members of Congress\u2014 (i) rules governing that implementation; and (ii) 1 or more reasonable extensions to achieve compliance with this subchapter, if the applicable supervising ethics committee determines that a Member of Congress is making a good faith effort to divest any covered financial instruments; and (B) guidance relating to covered financial instruments; (2) publishing on the internet certifications submitted by Members of Congress under section 13163(a); and (3) assessing civil fines against any Member of Congress who is in violation of this subchapter, subject to subsection (b). (b) Requirements for civil fines (1) In general Before imposing a fine pursuant to this section, the applicable supervising ethics committee shall provide to the applicable Member of Congress\u2014 (A) a written notice describing each covered financial instrument transaction for which a fine will be assessed; and (B) an opportunity, with respect to each such covered financial instrument transaction\u2014 (i) for a hearing; and (ii) to achieve compliance with the requirements of this subchapter. (2) Enforcement (A) In general In the event of continuing noncompliance after issuance of the notice described in paragraph (1), the applicable supervising ethics committee shall impose a civil penalty, in the amount described in subparagraph (B), on the Member of Congress to whom a notice was provided\u2014 (i) on the date that is 30 days after the date of provision of the notice; and (ii) during the period in which such noncompliance continues, not less frequently than once every 30 days thereafter. (B) Amount The amount of each civil penalty imposed on a Member of Congress pursuant to subparagraph (A) shall be an amount equal to 10 percent of the value of each covered financial instrument that was not divested in violation of this subchapter during the period covered by the penalty. (3) Publication Each supervising ethics committee shall publish on a publicly available website a description of\u2014 (A) each fine assessed by the supervising ethics committee pursuant to this section; (B) the reasons why each such fine was assessed; and (C) the result of each assessment, including any hearing under paragraph (1)(B)(i) relating to the assessment. (4) Appeal A Member of Congress may appeal the assessment of a fine under this section to a vote on the floor of the Senate or the House of Representatives, as applicable, as a privileged motion. 13165. Audit by Government Accountability Office Not later than 2 years after the date of enactment of the Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act , the Comptroller General of the United States shall\u2014 (1) conduct an audit of the compliance by Members of Congress with the requirements of this subchapter; and (2) submit to the supervising ethics committees a report describing the results of the audit conducted under paragraph (1). .\n##### (b) Conforming amendments\n**(1) Table of sections**\nThe table of sections for chapter 131 of title 5, United States Code, is amended by adding at the end the following:\nSUBCHAPTER IV\u2014Banning insider trading in Congress 13161. Definitions. 13162. Prohibition on certain transactions and holdings involving covered financial instruments. 13163. Certification of compliance. 13164. Authority of supervising ethics committees. 13165. Audit by Government Accountability Office. .\n**(2) Persons required to file**\nSection 13103(f) of title 5, United States Code, is amended\u2014\n**(A)**\nin paragraph (9), by striking as defined in section 13101 of this title ;\n**(B)**\nin paragraph (10), by striking as defined in section 13101 of this title ;\n**(C)**\nin paragraph (11), by striking as defined in section 13101 of this title ; and\n**(D)**\nin paragraph (12), by striking as defined in section 13101 of this title .",
      "versionDate": "2025-05-14",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-30",
        "text": "Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably."
      },
      "number": "1498",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-08-26T14:36:46Z"
          },
          {
            "name": "Commodities markets",
            "updateDate": "2025-08-26T14:36:46Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-26T14:36:46Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-08-26T14:36:46Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-08-26T14:36:46Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-08-26T14:36:46Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-26T14:36:46Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-08-26T14:36:46Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-08-26T14:36:46Z"
          },
          {
            "name": "Securities",
            "updateDate": "2025-08-26T14:36:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-28T12:55:21Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3388ih.xml"
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
      "title": "Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Elected Leaders from Owning Securities and Investments (PELOSI) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 131 of title 5, United States Code, to prohibit transactions involving certain financial instruments by Members of Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:48:36Z"
    }
  ]
}
```
