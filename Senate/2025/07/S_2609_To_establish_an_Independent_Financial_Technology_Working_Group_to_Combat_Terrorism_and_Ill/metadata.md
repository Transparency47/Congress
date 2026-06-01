# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2609?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2609
- Title: Financial Technology Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2609
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-04-20T15:22:32Z
- Update date including text: 2026-04-20T15:22:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2609",
    "number": "2609",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Financial Technology Protection Act of 2025",
    "type": "S",
    "updateDate": "2026-04-20T15:22:32Z",
    "updateDateIncludingText": "2026-04-20T15:22:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
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
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T18:51:30Z",
          "name": "Referred To"
        }
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "WY"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2609is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2609\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Budd (for himself, Ms. Lummis , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish an Independent Financial Technology Working Group to Combat Terrorism and Illicit Financing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Financial Technology Protection Act of 2025 .\n#### 2. Independent Financial Technology Working Group to Combat Terrorism and Illicit Financing\n##### (a) Establishment\nThere is established the Independent Financial Technology Working Group to Combat Terrorism and Illicit Financing (in this section referred to as the Working Group ), which shall consist of the following:\n**(1)**\nThe Secretary of the Treasury, acting through the Under Secretary for Terrorism and Financial Crimes, who shall serve as the chair of the Working Group.\n**(2)**\nA senior-level representative from each of the following:\n**(A)**\nThe Department of the Treasury.\n**(B)**\nThe Office of Terrorism and Financial Intelligence.\n**(C)**\nThe Internal Revenue Service.\n**(D)**\nThe Department of Justice.\n**(E)**\nThe Federal Bureau of Investigation.\n**(F)**\nThe Drug Enforcement Administration.\n**(G)**\nThe Department of Homeland Security.\n**(H)**\nThe United States Secret Service.\n**(I)**\nThe Department of State.\n**(J)**\nThe Office of the Director of National Intelligence.\n**(3)**\nAt least five individuals appointed by the Under Secretary for Terrorism and Financial Crimes to represent the following:\n**(A)**\nFinancial technology companies.\n**(B)**\nBlockchain intelligence companies.\n**(C)**\nFinancial institutions.\n**(D)**\nInstitutions or organizations engaged in research.\n**(E)**\nInstitutions or organizations focused on individual privacy and civil liberties.\n**(4)**\nSuch additional individuals as the Secretary of the Treasury may appoint as necessary to accomplish the duties described under subsection (b).\n##### (b) Duties\nThe Working Group shall\u2014\n**(1)**\nconduct research on terrorist and illicit use of digital assets and other related emerging technologies; and\n**(2)**\ndevelop legislative and regulatory proposals to improve anti-money laundering, counter-terrorist, and other counter-illicit financing efforts in the United States.\n##### (c) Reports\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, and annually for the 3 years thereafter, the Working Group shall submit to the Secretary of the Treasury, the heads of each agency represented in the Working Group pursuant to subsection (a)(2), and the appropriate congressional committees a report containing the findings and determinations made by the Working Group in the previous year and any legislative and regulatory proposals developed by the Working Group.\n**(2) Final report**\nBefore the date on which the Working Group terminates under subsection (d)(1), the Working Group shall submit to the appropriate congressional committees a final report detailing the findings, recommendations, and activities of the Working Group, including any final results from the research conducted by the Working Group.\n##### (d) Sunset\n**(1) In general**\nThe Working Group shall terminate on the later of\u2014\n**(A)**\nthe date that is 4 years after the date of the enactment of this Act; or\n**(B)**\nthe date on which the Working Group completes any wind-up activities described under paragraph (2).\n**(2) Authority to wind up activities**\nIf there are ongoing research, proposals, or other related activities of the Working Group ongoing as of the date that is 4 years after the date of the enactment of this Act, the Working Group may temporarily continue working in order to wind-up such activities.\n**(3) Return of appropriated funds**\nOn the date on which the Working Group terminates under paragraph (1), any unobligated funds appropriated to carry out this section shall be transferred to the Treasury.\n#### 3. Preventing rogue and foreign actors from evading sanctions\n##### (a) Report and strategy with respect to digital assets and other related emerging technologies\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the President, acting through the Secretary of the Treasury and in consultation with the head of each agency represented on the Independent Financial Technology Working Group to Combat Terrorism and Illicit Financing pursuant to section 2(a)(2), shall submit to the appropriate congressional committees a report that describes\u2014\n**(A)**\nthe potential uses of digital assets and other related emerging technologies by states, non-state actors, foreign terrorist organizations, and other terrorist groups to evade sanctions, finance terrorism, or launder monetary instruments, and threaten the national security of the United States; and\n**(B)**\na strategy for the United States to mitigate and prevent the illicit use of digital assets and other related emerging technologies.\n**(2) Form of report; public availability**\n**(A) In general**\nThe report required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n**(B) Public availability**\nThe unclassified portion of each report required by paragraph (1) shall be made available to the public and posted on a publicly accessible website of the Department of the Treasury\u2014\n**(i)**\nin precompressed, easily downloadable versions, in all appropriate formats; and\n**(ii)**\nin machine-readable format, if applicable.\n**(3) Sources of information**\nIn preparing the reports required by paragraph (1), the President may utilize any credible publication, database, or web-based resource, and any credible information compiled by any government agency, nongovernmental organization, or other entity that is made available to the President.\n##### (b) Briefing\nNot later than 2 years after the date of the enactment of this Act, the Secretary of the Treasury shall brief the appropriate congressional committees on the implementation of the strategy required by subsection (a)(1)(B).\n#### 4. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Banking, Housing, and Urban Affairs, the Committee on Finance, the Committee on Foreign Relations, the Committee on Homeland Security and Governmental Affairs, the Committee on the Judiciary, and the Select Committee on Intelligence of the Senate; and\n**(B)**\nthe Committee on Financial Services, the Committee on Foreign Affairs, the Committee on Homeland Security, the Committee on the Judiciary, the Committee on Ways and Means, and the Permanent Select Committee on Intelligence of the House of Representatives.\n**(2) Blockchain intelligence company**\nThe term blockchain intelligence company means any business providing software, research, or other services (such as blockchain tracing tools, geofencing, transaction screening, the collection of business data, and sanctions screening) that\u2014\n**(A)**\nsupport private and public sector investigations and risk management activities; and\n**(B)**\ninvolve cryptographically secured distributed ledgers or any similar technology or implementation.\n**(3) Digital asset**\nThe term digital asset means any digital representation of value that is recorded on a cryptographically secured digital ledger or any similar technology.\n**(4) Emerging technologies**\nThe term emerging technologies means the critical and emerging technology areas listed in the Critical and Emerging Technologies List developed by the Fast Track Action Subcommittee on Critical and Emerging Technologies of the National Science and Technology Council, including any updates to such list.\n**(5) Foreign terrorist organization**\nThe term foreign terrorist organization means an organization that is designated as a foreign terrorist organization under section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).\n**(6) Illicit use**\nThe term illicit use includes fraud, darknet marketplace transactions, money laundering, the purchase and sale of illicit goods, sanctions evasion, theft of funds, funding of illegal activities, transactions related to child sexual abuse material, and any other financial transaction involving the proceeds of specified unlawful activity (as defined in section 1956(c) of title 18, United States Code).\n**(7) Terrorist**\nThe term terrorist includes a person carrying out domestic terrorism or international terrorism (as such terms are defined, respectively, under section 2331 of title 18, United States Code).",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-07-22",
        "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2384",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Financial Technology Protection Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-18T19:08:07Z"
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
          "measure-id": "id119s2609",
          "measure-number": "2609",
          "measure-type": "s",
          "orig-publish-date": "2025-07-31",
          "originChamber": "SENATE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2609v00",
            "update-date": "2026-04-20"
          },
          "action-date": "2025-07-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Financial Technology Protection Act of 2025 </strong></p><p>This bill establishes the Independent Financial Technology Working Group to Combat Terrorism and Illicit Financing. The working group must study and report on terrorist and illicit use of digital assets and other related emerging technologies and develop proposals to improve anti-money laundering and counterterrorist financing efforts.</p><p>The working group terminates four years after the bill's enactment or after the working group completes any ongoing activities, whichever is later.</p><p>In addition, the Department of the Treasury must (1) report on the potential use of digital assets and other emerging technologies by states, nonstate actors, and terrorist groups for the purpose of evading sanctions to threaten the national security of the United States; and (2) describe a strategy to mitigate and prevent this usage.\u00a0</p>"
        },
        "title": "Financial Technology Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2609.xml",
    "summary": {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Financial Technology Protection Act of 2025 </strong></p><p>This bill establishes the Independent Financial Technology Working Group to Combat Terrorism and Illicit Financing. The working group must study and report on terrorist and illicit use of digital assets and other related emerging technologies and develop proposals to improve anti-money laundering and counterterrorist financing efforts.</p><p>The working group terminates four years after the bill's enactment or after the working group completes any ongoing activities, whichever is later.</p><p>In addition, the Department of the Treasury must (1) report on the potential use of digital assets and other emerging technologies by states, nonstate actors, and terrorist groups for the purpose of evading sanctions to threaten the national security of the United States; and (2) describe a strategy to mitigate and prevent this usage.\u00a0</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s2609"
    },
    "title": "Financial Technology Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Financial Technology Protection Act of 2025 </strong></p><p>This bill establishes the Independent Financial Technology Working Group to Combat Terrorism and Illicit Financing. The working group must study and report on terrorist and illicit use of digital assets and other related emerging technologies and develop proposals to improve anti-money laundering and counterterrorist financing efforts.</p><p>The working group terminates four years after the bill's enactment or after the working group completes any ongoing activities, whichever is later.</p><p>In addition, the Department of the Treasury must (1) report on the potential use of digital assets and other emerging technologies by states, nonstate actors, and terrorist groups for the purpose of evading sanctions to threaten the national security of the United States; and (2) describe a strategy to mitigate and prevent this usage.\u00a0</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s2609"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2609is.xml"
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
      "title": "Financial Technology Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Financial Technology Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an Independent Financial Technology Working Group to Combat Terrorism and Illicit Financing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:31Z"
    }
  ]
}
```
