# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8720?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8720
- Title: Campaign Finance Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 8720
- Origin chamber: House
- Introduced date: 2026-05-11
- Update date: 2026-05-19T22:34:49Z
- Update date including text: 2026-05-19T22:34:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-11: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 11 - 0.
- Latest action: 2026-05-11: Introduced in House

## Actions

- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 11 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-11",
    "latestAction": {
      "actionDate": "2026-05-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8720",
    "number": "8720",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001213",
        "district": "1",
        "firstName": "Bryan",
        "fullName": "Rep. Steil, Bryan [R-WI-1]",
        "lastName": "Steil",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Campaign Finance Transparency Act",
    "type": "HR",
    "updateDate": "2026-05-19T22:34:49Z",
    "updateDateIncludingText": "2026-05-19T22:34:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 11 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-11",
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
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-11",
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
            "date": "2026-05-14T17:14:06Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-11T14:30:35Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8720ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8720\nIN THE HOUSE OF REPRESENTATIVES\nMay 11, 2026 Mr. Steil introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to modify requirements regarding contributions related to elections for Federal office and to improve the operation of the Federal Election Commission, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Campaign Finance Transparency Act .\n#### 2. Requiring disclosure of card verification value or card verification code as condition of acceptance of online contributions made using credit or debit cards in Federal elections\nSection 302 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30102 ) is amended by adding at the end the following:\n(j) (1) No political committee shall accept any internet credit or debit card contribution unless\u2014 (A) except in the case of a contribution the political committee receives by mail, the individual or entity making such contribution is required, at the time such individual or entity makes such contribution, to disclose the card verification value or card verification code of such credit or debit card and the ZIP Code of the billing address associated with such credit or debit card; and (B) (i) the mailing address of the individual or entity is located in a State; or (ii) in the case of a contribution made by an individual whose mailing address is not located in a State, the individual provides the committee with the applicable information described in paragraph (2). (2) The applicable information described in this paragraph is as follows: (A) In the case of an individual who is a citizen or national of the United States\u2014 (i) the United States mailing address the individual uses for voter registration purposes; (ii) a copy of the individual\u2019s United States passport; or (iii) a copy of a comparable acceptable identification document, or the unique identifying number from such a document, for the individual. (B) In the case of an individual who is lawfully admitted for permanent residence, as defined by section 101(a)(20) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(20) )\u2014 (i) a copy of the individual\u2019s permanent resident card; or (ii) a copy of a comparable acceptable identification document issued by the Department of Homeland Security. (3) A political committee that accepts any internet credit or debit card contribution as a recurring contribution shall require the individual or entity making such contribution to comply with the requirements of this subsection for the first such contribution, but shall not require the individual or entity to provide the information identified in paragraphs (1) and (2) for subsequent recurring contributions made using the same credit or debit card as the initial contribution. (4) A political committee that stores or saves, or arranges to store or save, any credit or debit card information shall require the individual or entity making such contribution to comply with the requirements of this subsection for the first such contribution or at the time of storing or saving such information, but shall not require the individual or entity to provide the information identified in paragraphs (1) and (2) for subsequent contributions made using the same credit or debit card as the initial contribution. (5) An internet credit or debit card contribution received by a political committee made through the use of a digital wallet shall be treated as complying with the requirements of this subsection. (6) Notwithstanding subsection (b) or (c), in the case of an internet credit or debit card contribution\u2014 (A) no later than 10 days after receiving the contribution, the person who receives the contribution shall forward to the treasurer such contribution, the name and address of the person making the contribution, and the date of receipt; and (B) the treasurer of a political committee shall keep an account of the name and address of any person making any such contribution, together with the date and amount of such contribution by any person consistent with applicable regulations of the Commission, including regulations relating to the period for which contribution records must be preserved and the anonymity of certain contributors. (7) (A) A treasurer of a political committee who is aware that a contribution to the committee is not in compliance with this subsection has an affirmative duty to refund the contribution to the individual or entity making the contribution. (B) If the treasurer of a political committee shows that best efforts have been used to comply with the requirements of this paragraph, the committee shall be considered in compliance with this subsection. (8) In this subsection\u2014 (A) the term digital wallet means a software application that stores payment or account information to facilitate traditional payments that use bank and credit card information; and (B) the term Internet credit or debit card contribution means a contribution that\u2014 (i) is made using a credit or debit card; and (ii) is received through an internet website or application. .\n#### 3. Requiring name on credit or debit card to be name of donor as condition of acceptance of contributions in Federal elections\nSection 302 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30102 ), as amended by section 2 , is amended by adding at the end the following:\n(k) No political committee shall accept any credit or debit card contribution unless the name on the credit or debit card used to make such contribution is the name of the individual or entity donating such contribution. .\n#### 4. Prohibiting acceptance of contributions made using gift cards in Federal elections\nSection 302 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30102 ), as amended by section 2 and section 3, is amended by adding at the end the following:\n(l) No political committee shall knowingly accept a contribution made through the use of a gift certificate or store gift card, as such terms are defined, respectively, under section 915(a) of the Electronic Fund Transfer Act. (2) (A) A treasurer of a political committee who is aware that a contribution to the committee is not in compliance with this subsection has an affirmative duty to refund the contribution to the individual or entity making the contribution. (B) If the treasurer of a political committee shows that best efforts have been used to comply with the requirements of this subsection, the committee shall be considered in compliance with this subsection. .\n#### 5. Removal of threshold for reporting contributions\nSection 304 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30104 ) is amended\u2014\n**(1)**\nin subsection (b)(3)\u2014\n**(A)**\nin subparagraph (A), by striking whose contribution or contributions have an aggregate amount or value in excess of $200 within the calendar year (or election cycle, in the case of an authorized committee of a candidate for Federal office), or in any lesser amount if the reporting committee should so elect, ;\n**(B)**\nin subparagraph (F), by striking in an aggregate amount or value in excess of $200 within the calendar year (or election cycle, in the case of an authorized committee of a candidate for Federal office) ; and\n**(C)**\nin subparagraph (G), by striking in an aggregate value or amount in excess of $200 within the calendar year (or election cycle, in the case of an authorized committee of a candidate for Federal office) ;\n**(2)**\nin subsection (c)(2)(C), by striking in excess of $200 ; and\n**(3)**\nin subsection (e)(3)\u2014\n**(A)**\nby striking receipts or ; and\n**(B)**\nby striking paragraphs (3)(A), (5), and inserting paragraphs (5) .\n#### 6. Prohibiting aiding or abetting making of contribution in the name of another\nSection 320 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30122 ) is amended\u2014\n**(1)**\nby striking No person and inserting the following:\n(a) In general No person ; and\n**(2)**\nby adding at the end the following:\n(b) Prohibition on assistance No person shall knowingly direct, help, or assist any person in making a contribution in the name of another person. (c) Reporting of suspected contributions Any recipient who suspects that a contribution made to such recipient is a contribution made by one person in the name of another person shall report such contribution to the Federal Election Commission. .\n#### 7. Regulations\n##### (a) Deadline\nNot later than 90 days after the date of the enactment of this Act, the Federal Election Commission shall promulgate regulations to carry out the amendments made by this Act.\n##### (b) Consultation with credit card payment networks\nIn promulgating regulations under subsection (a) to carry out the amendments made by this Act, the Commission shall consult with representatives of payment card networks, as defined under section 921(c) of the Electronic Fund Transfer Act ( 15 U.S.C. 1693o\u20132(c) ), and other relevant stakeholders.\n#### 8. Effective date\nThe amendments made by this Act shall apply with respect to contributions made after the expiration of the 90-day period which begins on the date the Commission promulgates regulations under section 7 .",
      "versionDate": "2026-05-11",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-19T22:34:49Z"
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
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8720ih.xml"
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
      "title": "Campaign Finance Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T05:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Campaign Finance Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-13T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to modify requirements regarding contributions related to elections for Federal office and to improve the operation of the Federal Election Commission, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T05:33:29Z"
    }
  ]
}
```
