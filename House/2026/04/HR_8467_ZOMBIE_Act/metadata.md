# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8467?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8467
- Title: ZOMBIE Act
- Congress: 119
- Bill type: HR
- Bill number: 8467
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-05T20:22:16Z
- Update date including text: 2026-05-05T20:22:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8467",
    "number": "8467",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000609",
        "district": "6",
        "firstName": "Gary",
        "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
        "lastName": "Palmer",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "ZOMBIE Act",
    "type": "HR",
    "updateDate": "2026-05-05T20:22:16Z",
    "updateDateIncludingText": "2026-05-05T20:22:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
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
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
            "date": "2026-04-29T13:07:47Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-23T13:02:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8467ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8467\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Palmer introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo reform the Payment Integrity Information Act of 2019 to ensure executive agencies focus on fraud prevention, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Zeroing Out Monetary Benefits Improperly Expended Act or the ZOMBIE Act .\n#### 2. Reforms to Payment Integrity Information Act of 2019\n##### (a) Definitions\nSection 3351 of title 31, United States Code, is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (i)\u2014\n**(I)**\nby inserting information on before improper payments ;\n**(II)**\nby striking information with and inserting resulting in financial loss to the Government with ; and\n**(III)**\nby striking and at the end; and\n**(ii)**\nby inserting after clause (ii) the following new clause:\n(iii) published information on improper payments resulting in financial loss to the Government with the annual budget justification of the executive agency for the most recent fiscal year; ;\n**(B)**\nby redesignating subparagraphs (B) and (C) as clauses (iv) and (v), respectively (and by redesignating subparagraphs (D) through (F) as subparagraphs (B) through (D), respectively);\n**(C)**\nin subparagraph (A)(iv), as so redesignated, by striking if required, has ;\n**(D)**\nin subparagraph (A)(v), as so redesignated, by striking if required, publishes and inserting published ;\n**(E)**\nby striking subparagraph (B), as so redesignated; and\n**(F)**\nby redesignating subparagraphs (C) and (D), as so redesignated, as subparagraphs (B) and (C); and\n**(2)**\nby adding at the end the following new paragraph:\n(9) Financial loss to the Government The term financial loss to the Government \u2014 (A) means any payment or part of a payment made in excess of the correct amount authorized by law that results in a financial loss to the Federal Government; and (B) does not include any payment or part of a payment made to the correct person or entity for the correct amount authorized by law but not made in accordance with certain administrative procedures applicable to the executive agency (excluding any such procedure necessary to establish eligibility or to verify that any payment or part of a payment was made in such correct amount). .\n##### (b) Estimates of improper payments resulting in financial loss to the Government and reports on actions to reduce such payments\nSection 3352 of title 31, United States Code, is amended\u2014\n**(1)**\nin the heading\u2014\n**(A)**\nby inserting resulting in financial loss to the Government before and reports ; and\n**(B)**\nby striking reduce improper payments and inserting reduce such payments ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by striking periodically review all programs and activities and inserting submit annually a list of each program and activity required to be reported on the Program Inventory under section 1122 ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby striking all programs and activities and inserting each program and activity from each such list ; and\n**(II)**\nby striking (3) and inserting (2) ;\n**(B)**\nby striking paragraph (2);\n**(C)**\nby redesignating paragraph (3) as paragraph (2); and\n**(D)**\nin paragraph (2), as so redesignated\u2014\n**(i)**\nin subparagraph (A), by striking improper payments and payments whose propriety cannot be determined and inserting improper payments resulting in financial loss to the Government and payments lacking sufficient documentation to determine whether the payments result in financial loss to the Government ;\n**(ii)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (D) and (E), respectively;\n**(iii)**\nby inserting after subparagraph (A) the following new subparagraphs:\n(B) Development of risk assessment guidance Not later than 1 year after the date of the enactment of this Act, the Secretary of the Treasury shall develop risk assessment guidance to assess the risk of improper payments resulting in financial loss to the Government that addresses the following: (i) The likelihood of payment errors and the magnitude of such errors that do not result in financial loss to the Government. (ii) The likelihood of payment errors and the magnitude of such errors that do result in financial loss to the Government. (iii) A formula for estimating financial loss to the Government. (iv) Relevant governmentwide documents and best practices for managing improper payments and mitigating fraud risks in Federal programs, such as the document of the Government Accountability Office entitled A Framework for Managing Fraud Risks in Federal Programs (or any successor document), as applicable and appropriate. (C) Scope In preparing a list under paragraph (1)(A), the head of each executive agency shall require, within 6 months after issuing the risk assessment guidance, a risk assessment using the guidance developed under subparagraph (B) for each program or activity listed under paragraph (1)(A) for each\u2014 (i) existing programs or activities prior to the next disbursement of Federal funds with respect to the program or activity; and (ii) newly authorized programs and activities prior to any disbursement of Federal funds with respect to the program or activity. ;\n**(iv)**\nin subparagraph (D), as so redesignated\u2014\n**(I)**\nin the heading, by striking Scope and inserting Requirements ;\n**(II)**\nin the matter preceding clause (i)\u2014\n**(aa)**\nby striking In conducting a review under paragraph (1), the head of each executive agency shall and inserting Risk assessments are to be conducted on an ongoing basis, but no less frequently than once every 3 years, and ; and\n**(bb)**\nby inserting , including with respect to fraud in any program or activity listed under paragraph (1)(A) that causes improper payments resulting in financial loss to the Government before , such as ;\n**(III)**\nin clause (x), by striking data systems and inserting data assets ; and\n**(IV)**\nin clause (xi)\u2014\n**(aa)**\nby inserting or improper payments before as assessed ; and\n**(bb)**\nby inserting , or any successor document after (commonly known as the Green Book ) ; and\n**(v)**\nin subparagraph (E), as so redesignated\u2014\n**(I)**\nin the heading, by striking Annual report and inserting Reports ;\n**(II)**\nin the matter preceding clause (i), by striking Each executive agency shall publish an annual report and inserting Not less than once every 3 years, the head of each executive agency shall publish a report ;\n**(III)**\nin clause (i), by striking ; and and inserting a semicolon;\n**(IV)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(V)**\nby adding at the end the following new clause:\n(iii) a prioritized listing of risks identified in subparagraph (D) associated with each program and activity listed under paragraph (1)(A) and any corresponding financial and administrative control to mitigate any such risk, including the use of the Do Not Pay Initiative (or any successor system) and any other system or data asset maintained by the Secretary of the Treasury or the Inspector General of the executive agency to prevent fraud or improper payments resulting in financial loss to the Government prior to making an eligibility determination to receive Federal funds with respect to any such program or activity listed under paragraph (1)(A), issuing an award, or requesting a payment. ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin the heading, by inserting that result in financial loss to the Government after improper payments ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby redesignating subparagraphs (A) and (B) as subparagraphs (B) and (C), respectively;\n**(ii)**\nby inserting before subparagraph (B), as so redesignated, the following new subparagraph:\n(A) review each statistically valid estimate developed under subsection (c)(1)(A) and make a recommendation to the head of the executive agency on whether the agency estimate should be reassessed and reestablished; ;\n**(iii)**\nin subparagraph (B)\u2014\n**(I)**\nby inserting and activities after high-priority Federal programs ; and\n**(II)**\nby inserting that result in financial loss after improper payments each place it appears; and\n**(iv)**\nin subparagraph (C)\u2014\n**(I)**\nby striking (A) and inserting (B) ; and\n**(II)**\nby striking associated and inserting and financial loss associated ; and\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nin the heading, by inserting that result in financial loss to the Government after improper payments ;\n**(ii)**\nin subparagraph (A), by striking shall on an annual basis and inserting , not less frequently than once every 3 years, shall ;\n**(iii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nin subclause (I)\u2014\n(AA)\nby inserting that result in financial loss to the Government after improper payments ; and\n(BB)\nby striking ; and and inserting a semicolon;\n**(bb)**\nin subclause (II), by inserting that result in financial loss to the Government, including by making it harder for fraudulent actors to exploit the program after improper payments ; and\n**(cc)**\nby adding at the end the following new subclause:\n(III) has taken or plans to take to reduce the percentage of improper payments that result in financial loss to the Government; ; and\n**(II)**\nby inserting after clause (i) the following new clause (and redesignating the succeeding clause accordingly):\n(ii) shall include\u2014 (I) an estimate of the total amount of the payments that result in financial loss to the Government; (II) an estimate of the total amount of the payments that do not result in financial loss to the Government; (III) the percentage of payments that result in financial loss to the Government; (IV) an assessment of the portion of the total amount of payments that result in financial loss to the Government that are due to fraudulent actions by the recipient of such payments; (V) the total amount of disbursed payments; and (VI) a description of resources or legislative changes proposed to improve or maintain the integrity of the relevant program or activity; and ;\n**(iv)**\nin subparagraph (E)(i)\u2014\n**(I)**\nin subclause (I), by striking improper payment and inserting improper payments that result in financial loss ; and\n**(II)**\nin subclause (II), by striking improper payments and inserting improper payments that result in financial loss ; and\n**(v)**\nby amending subparagraph (F) to read as follows:\n(F) Agency liaison designation and mandatory coordination meetings Not less frequently than once every fiscal year, the head of each executive agency with a high-priority Federal program or activity identified under paragraph (1)(B) shall designate a senior official of the executive agency to serve as the liaison of the executive agency for work under this subchapter who shall meet for a non-audit or investigative purpose with the Director of the Office of Management and Budget (or a designee of the Director), the Commissioner of the Bureau of the Fiscal Service of the Department of the Treasury (or a designee of the Commissioner), the Inspector General of the executive agency (or a designee of the Inspector General), and the Pandemic Response Accountability Committee established under section 15010 of the CARES Act ( Public Law 116\u2013136 ; 134 Stat. 533) (or any successor organization) to report on any action taken during the preceding fiscal year and any planned action, including any reform to any financial or administrative control, to prevent improper payments (with a focus on improper payments that lead to financial loss to the Government) and mitigate fraud in such program or activity. ;\n**(4)**\nin subsection (c)\u2014\n**(A)**\nin the heading, by inserting that result in financial loss to the Government after improper payments ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby amending subparagraph (A) to read as follows:\n(A) develop a statistically valid estimate of improper payments that result in financial loss to the Government; ;\n**(ii)**\nby striking subparagraph (B); and\n**(iii)**\nby adding at the end the following new subparagraphs:\n(B) include such estimate in the annual budget justification of the executive agency; and (C) revise such estimate if the head of the executive agency determines, which may be based on a recommendation from the Director in consultation with the Secretary of the Treasury and the Inspector General of the executive agency, that there is a need to reestablish the estimate of improper payments that result in financial loss to the Government due to\u2014 (i) a significant change, as determined by the agency head, to the program or activity\u2019s appropriation or authorization; (ii) newly establishing the program or activity; or (iii) a recommendation from the agency Inspector General in the annual compliance report issued under section 3353(a). ; and\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by inserting resulting in financial loss to the Government, after improper payment ; and\n**(ii)**\nin subparagraph (B), by striking improper payments before estimate ;\n**(5)**\nin subsection (d)\u2014\n**(A)**\nin the heading\u2014\n**(i)**\nby striking reduce and inserting reduce and prevent ; and\n**(ii)**\nby inserting that result in financial loss to the Government after improper payments ;\n**(B)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby inserting that result in financial loss to the Government after estimated improper payments ; and\n**(ii)**\nby striking reduce improper payments and inserting reduce and prevent such payments ;\n**(C)**\nin paragraph (1), by inserting that result in financial loss to the Government (including actions used to commit fraud) after improper payments ;\n**(D)**\nin paragraph (2)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting that result in financial loss to the Government after in order to reduce improper payments ;\n**(ii)**\nin subparagraph (B), by striking ; and and inserting a semicolon at the end;\n**(iii)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(iv)**\nby adding at the end the following new subparagraph:\n(D) access to appropriate records and data assets, whether maintained by an executive agency, a State or local government, or a private sector organization; ;\n**(E)**\nin paragraph (5), by striking ; and and inserting a semicolon at the end;\n**(F)**\nin paragraph (6), by striking the period at the end and inserting ; and ; and\n**(G)**\nby adding at the end the following new paragraph:\n(7) information on the progress of the executive agency with respect to\u2014 (A) implementing the financial and administrative controls required to be established under subsection (a)(2)(E)(iii); (B) implementing relevant governmentwide documents and best practices for managing improper payments and mitigating fraud risks in Federal programs, such as the document of the Government Accountability Office entitled A Framework for Managing Fraud Risks in Federal Programs (or any successor document), as applicable and appropriate, including with respect to the identification of\u2014 (i) any dedicated entity that leads the fraud risk management activity of the executive agency; (ii) responsibilities of such entity, including any program or operation for which the entity is responsible; (iii) capacity, including any limitations, to strategically manage fraud risks; (iv) any program or operation within the executive agency for which there is not a dedicated entity that leads fraud risk management, along with a detailed justification for not having such a dedicated entity; and (v) the status of implementing the overarching concepts with associated leading practices identified in such document entitled A Framework for Managing Fraud Risks in Federal Programs (or any such successor document), as applicable and appropriate; (C) implementing the Office of Management and Budget Circular A\u2013123, or any successor policy, with respect to leading practices for managing fraud and improper payments risk; (D) identifying fraud risks and vulnerabilities, including but not limited to payroll, beneficiary payments, grants, large contracts, and purchase and travel cards; and (E) establishing strategies, procedures, and other steps to prevent, detect, and respond to fraud. ;\n**(6)**\nin subsection (e)\u2014\n**(A)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby inserting that result in financial loss to the Government, after With respect to improper payments ; and\n**(ii)**\nby striking the improper payments and inserting such payments ;\n**(B)**\nin paragraph (1), by inserting that result in financial loss to the Government, after improper payments ; and\n**(C)**\nin paragraph (2), by inserting that result in financial loss to the Government, after improper payments ;\n**(7)**\nin subsection (f)(1)\u2014\n**(A)**\nin the matter preceding subparagraph (A)\u2014\n**(i)**\nby inserting that result in financial loss to the Government after regarding improper payments ; and\n**(ii)**\nby inserting such after recover ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby inserting Government before Reform ; and\n**(ii)**\nby striking and at the end; and\n**(C)**\nby inserting after subparagraph (B) the following new subparagraphs (and redesignating the succeeding subparagraph accordingly):\n(C) the Committee on the Budget of the Senate; (D) the Committee on the Budget of the House of Representatives; (E) the Committee on Appropriations of the Senate; (F) the Committee on Appropriations of the House of Representatives; and ;\n**(8)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1), by inserting and periodically thereafter, after Not later than 1 year after the date of enactment of this section ; and\n**(B)**\nin paragraph (2)(B), by striking prepayment and postpayment and inserting pre-award and pre-payment ; and\n**(9)**\nin subsection (i)(2)\u2014\n**(A)**\nin subparagraph (C), by striking 25 and inserting 10 ; and\n**(B)**\nin subparagraph (D), by striking 25 and inserting 75 .",
      "versionDate": "2026-04-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2026-05-05T20:22:11Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-05T20:22:16Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-05-05T20:21:57Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-05T20:22:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-27T23:03:08Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8467ih.xml"
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
      "title": "ZOMBIE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ZOMBIE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-24T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Zeroing Out Monetary Benefits Improperly Expended Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-24T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reform the Payment Integrity Information Act of 2019 to ensure executive agencies focus on fraud prevention, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-24T08:18:38Z"
    }
  ]
}
```
