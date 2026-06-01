# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2253?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2253
- Title: Unsubscribe Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2253
- Origin chamber: Senate
- Introduced date: 2025-07-10
- Update date: 2026-04-14T20:29:16Z
- Update date including text: 2026-04-14T20:29:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in Senate
- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-07-10: Introduced in Senate

## Actions

- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2253",
    "number": "2253",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001194",
        "district": "",
        "firstName": "Brian",
        "fullName": "Sen. Schatz, Brian [D-HI]",
        "lastName": "Schatz",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Unsubscribe Act of 2025",
    "type": "S",
    "updateDate": "2026-04-14T20:29:16Z",
    "updateDateIncludingText": "2026-04-14T20:29:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T18:09:27Z",
          "name": "Referred To"
        }
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
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2253is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2253\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mr. Schatz (for himself and Mr. Kennedy ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo increase consumer protection with respect to negative options in all media, including on the internet, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unsubscribe Act of 2025 .\n#### 2. Increased consumer protection with respect to negative options\n##### (a) Disclosure of negative options\nIt shall be unlawful for any merchant of record to charge or attempt to charge a credit card, debit card, bank account, or other financial account of any consumer, or otherwise receive payment from any consumer, through a negative option, unless the merchant of record clearly and conspicuously discloses all material terms of the contract involved before receiving payment or charging the consumer, or otherwise receiving payment, through such negative option.\n##### (b) Express informed consent for negative options\n**(1) Requirement**\nIt shall be unlawful for any merchant of record to charge or attempt to charge a credit card, debit card, bank account, or other financial account of any consumer, or otherwise receive payment from any consumer, through a negative option, unless the merchant of record obtains the express informed consent of the consumer before receiving payment or charging the consumer, or otherwise receiving payment, through such negative option.\n**(2) Duration**\nA merchant of record shall keep or maintain verification of the express informed consent obtained pursuant to paragraph (1) for not fewer than 3 years, unless such merchant of record demonstrates by a preponderance of the evidence that the merchant of record uses processes that ensure a consumer may not technologically complete a transaction without such express informed consent.\n##### (c) Term limitation for negative option contracts\nAfter the expiration of a preliminary period, it shall be unlawful for any merchant of record to automatically renew or otherwise continue a negative option contract with any consumer for a period that is greater than the length of the preliminary period, unless such merchant of record, at the time of such expiration, obtains the express informed consent of the consumer to renew or otherwise continue such negative option contract.\n##### (d) Cancellation of negative option contracts\n**(1) Online merchants**\nIn the case of a negative option contract that is entered into electronically, it shall be unlawful for any merchant of record to enter into such negative option contract with any consumer unless such merchant of record provides to the consumer a simple mechanism, including a direct link to an electronic form, that enables the consumer to submit a request to cancel such negative option contract without requiring the consumer to take additional steps by any means other than electronically.\n**(2) Other merchants**\nIn the case of a negative option contract that is entered into through means other than electronically, it shall be unlawful for any merchant of record to enter into such negative option contract with any consumer unless such negative option contract provides the consumer with a simple mechanism for cancellation, in the same manner, and by the same means, as such negative option contract was entered into, or, if not practicable, through some other simple mechanism for cancellation.\n##### (e) Requirements for free-To-Pay conversion contracts\nIt shall be unlawful for any merchant of record to charge or attempt to charge a credit card, debit card, bank account, or other financial account of any consumer for any good or service sold under a free-to-pay conversion contract, unless each of the following is met:\n**(1)**\nBefore completing the financial transaction, or otherwise receiving payment, the merchant of record provides the consumer with a notification of the terms of the negative option contract and obtains the express informed consent of the consumer to such terms, including the following terms:\n**(A)**\nFor an introductory period, the consumer will receive the good or service at no cost or for a discounted cost.\n**(B)**\nThe amount the consumer will be charged or otherwise required to pay for the introductory period.\n**(C)**\nThe amount the consumer will be charged or otherwise required to pay, on a recurring basis, starting with the first financial transaction after the introductory period.\n**(D)**\nThe total cost (or range of costs) the consumer will be charged or otherwise required to pay through the entire term of such contract (if such term is less than 12 months) or cost information that enables the consumer to determine the total cost for the subsequent 12-month period, to the extent known.\n**(2)**\nBefore the first charge, payment, or price increase after the introductory period, the merchant of record provides notification to the consumer about the upcoming charge, payment, or increase and provides the consumer with\u2014\n**(A)**\nthe terms of the negative option contract, including the length of time required for the merchant of record to complete any cancellation request; and\n**(B)**\ndirect access to information about the simple mechanism for cancellation.\n##### (f) Other notification requirements for negative option contracts\n**(1) General notification and access**\nWith respect to any negative option contract entered into by a merchant of record and a consumer, the merchant of record, at regular intervals as determined by the Commission (but not less frequently than annually) while such negative option contract remains in effect, shall provide the consumer with\u2014\n**(A)**\na notification of the terms of such negative option contract; and\n**(B)**\ndirect access to information about the simple mechanism for cancellation.\n**(2) Additional notification and access**\nIf a negative option contract specifies a period of time during which the merchant of record shall complete a cancellation request, not fewer than 2 but not more than 7 days before the last day on which the consumer may cancel such negative option contract without incurring additional charges, the merchant of record shall provide the consumer with the notification and access required by paragraph (1).\n#### 3. Enforcement\n##### (a) Enforcement by the Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act or a regulation promulgated thereunder shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates this Act or a regulation promulgated thereunder shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n**(D) Rulemaking**\nThe Commission shall promulgate in accordance with section 553 of title 5, United States Code, such rules as may be necessary to carry out this Act.\n##### (b) Enforcement by States\n**(1) In general**\nIf the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of the State has been or is being threatened or adversely affected by a practice that violates this Act, the State may bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief.\n**(2) Rights of the Commission**\n**(A) Notice to the Commission**\n**(i) In general**\nExcept as provided in clause (iii), an attorney general, official, or agency of a State, before initiating a civil action under paragraph (1), shall provide a written notice to the Commission that the attorney general, official, or agency intends to bring such civil action.\n**(ii) Contents**\nThe notice required by clause (i) shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for an attorney general, official, or agency of a State to provide the notice required by clause (i) before initiating a civil action under paragraph (1), the attorney general, official, or agency shall provide such notice to the Commission immediately upon instituting the civil action.\n**(B) Intervention by the Commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by an attorney general, official, or agency of a State under paragraph (1); and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nappeal a decision in the civil action.\n**(C) Limitation on State action while Federal action is pending**\nIf the Commission or the Attorney General of the United States has instituted a civil action for violation of this Act (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under paragraph (1) during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of such Act alleged in such complaint.\n**(3) Rule of construction**\nNothing in this subsection may be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n#### 4. Preemption of directly conflicting State laws\n##### (a) In general\nNothing in this Act may be construed to preempt, displace, or supplant any State law, except to the extent that a provision of State law conflicts with a provision of this Act, and then only to the extent of the conflict.\n##### (b) Greater protection under State law\nFor purposes of this section, a provision of State law does not conflict with a provision of this Act if such provision of State law provides additional protections to consumers protected under this Act.\n##### (c) Conflicting time frames\nAny difference between Federal and State law in the time frame in which a requirement imposed on a person shall be met shall be considered a conflict for purposes of subsection (a).\n#### 5. Definitions\nIn this Act:\n**(1) Automatic renewal contract**\nThe term automatic renewal contract means a contract between any merchant of record and any consumer for the sale of goods or services that is automatically renewed after a preliminary period, unless the consumer instructs otherwise.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Continuity plan contract**\nThe term continuity plan contract means a contract between any merchant of record and any consumer under which the consumer agrees to pay for periodic shipments of goods or the provision of services, unless the consumer instructs otherwise.\n**(4) Express informed consent**\n**(A) In general**\nThe term express informed consent means, with respect to an offer or agreement for the sale of goods or services that includes a negative option, an affirmative action taken by a consumer, including clicking on a confirmation button or checking a box, that\u2014\n**(i)**\nindicates the unambiguous consent of the consumer to the negative option; and\n**(ii)**\nis separate and apart from any action taken by the consumer to indicate the initial consent of the consumer to all of the material terms of the offer or agreement (including to be charged for the preliminary period), but may occur at the same time as such initial consent.\n**(B) Exclusions**\nThe term express informed consent shall not include\u2014\n**(i)**\nconsent that is inferred through the inactivity or silence of a consumer or the use of pre-checked boxes with respect to an initial charge or any recurring charge; or\n**(ii)**\nconsent obtained through a user interface designed or manipulated to have the substantial effect of subverting or impairing user autonomy, decision-making, or choice.\n**(5) Free-to-pay conversion contract**\nThe term free-to-pay conversion contract means a contract for the sale of goods or services between any merchant of record and any consumer that includes an introductory period.\n**(6) Introductory period**\nThe term introductory period means a preliminary period of a contract for the sale of goods or services where\u2014\n**(A)**\nduring such period, the consumer receives a good or service at no charge or for a discounted cost; and\n**(B)**\nat the expiration of such period, the amount the consumer will be charged or otherwise be required to pay for the good or service is increased.\n**(7) Merchant of record**\nThe term merchant of record means a person who enters into a financial contract with a consumer.\n**(8) Negative option**\nThe term negative option means a provision of an offer or agreement for the sale of goods or services under which the silence of a consumer or failure by a consumer to take an affirmative action to reject the goods or services or to cancel the agreement is interpreted by the seller as acceptance of the offer or renewal of the agreement.\n**(9) Negative option contract**\nThe term negative option contract means a contract that includes a negative option, including\u2014\n**(A)**\nan automatic renewal contract;\n**(B)**\na continuity plan contract;\n**(C)**\na free-to-pay conversion contract;\n**(D)**\na pre-notification negative option plan contract; and\n**(E)**\nany combination of the contracts described in subparagraphs (A) through (D).\n**(10) Notification**\nThe term notification , when used with respect to the terms of a contract, means a written notification that clearly, conspicuously, and concisely states all material terms of the negative option, including information regarding the simple mechanism for cancellation and the length of time required for a merchant of record to complete any cancellation request.\n**(11) Preliminary period**\nThe term preliminary period means the period of a negative option contract prior to the date on which a negative option takes effect.\n**(12) Pre-notification negative option plan contract**\nThe term pre-notification negative option plan contract means a contract between any merchant of record and any consumer under which the consumer receives periodic notices offering goods or services and, unless the consumer specifically rejects the offer, the consumer automatically receives the goods and services and agrees to pay for such goods and services.\n**(13) Simple mechanism**\nThe term simple mechanism means the term described in section 425.6 of title 16, Code of Federal Regulations, or any successor regulation.\n#### 6. Effective date\nThis Act shall apply with respect to contracts entered into or amended after the date that is 1 year after the date of the enactment of this Act.",
      "versionDate": "2025-07-10",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-01-13",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "7048",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Unsubscribe Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-07-30T23:06:46Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2253is.xml"
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
      "title": "Unsubscribe Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Unsubscribe Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase consumer protection with respect to negative options in all media, including on the internet, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:33:25Z"
    }
  ]
}
```
