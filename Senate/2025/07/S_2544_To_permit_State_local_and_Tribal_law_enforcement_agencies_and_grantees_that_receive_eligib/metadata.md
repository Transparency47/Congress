# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2544?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2544
- Title: GUARD Act
- Congress: 119
- Bill type: S
- Bill number: 2544
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-03-27T15:50:19Z
- Update date including text: 2026-03-27T15:50:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-02-05 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2026-02-09 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-02-09 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-02-09 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 317.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-02-05 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2026-02-09 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-02-09 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-02-09 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 317.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2544",
    "number": "2544",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001319",
        "district": "",
        "firstName": "Katie",
        "fullName": "Sen. Britt, Katie Boyd [R-AL]",
        "lastName": "Britt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "GUARD Act",
    "type": "S",
    "updateDate": "2026-03-27T15:50:19Z",
    "updateDateIncludingText": "2026-03-27T15:50:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 317.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
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
      "actionDate": "2025-07-30",
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
            "date": "2026-02-09T23:39:39Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-05T15:15:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-30T19:34:37Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-30T19:34:37Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "FL"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "OK"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "DE"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "IA"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2544is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2544\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mrs. Britt (for herself, Mrs. Gillibrand , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo permit State, local, and Tribal law enforcement agencies and grantees that receive eligible Federal grant funds to use such funds for investigating elder financial fraud, pig butchering, and general financial fraud, and to clarify that Federal law enforcement agencies may assist State, local, and Tribal law enforcement agencies in the use of tracing tools for blockchain and related technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarding Unprotected Aging Retirees from Deception Act or the GUARD Act .\n#### 2. Definitions\nIn this Act:\n**(1) Elder financial fraud**\nThe term elder financial fraud means the illegal or improper use of the money, property, or other resources of an elderly individual or adult with a disability for monetary or personal benefit, profit, or gain.\n**(2) Eligible Federal grant funds**\nThe term eligible Federal grant funds means funds received under any of the following:\n**(A)**\nTitle IV of the Prioritizing Resources and Organization for Intellectual Property Act of 2008 ( 34 U.S.C. 30103 et seq. ) (commonly known as the Economic, High-Technology, White Collar, and Internet Crime Prevention National Training and Technical Assistance Program ), including relating to the use of technology to solve crimes and to facilitate prosecutions (commonly known as the Internet of Things (IoT) National Training and Technical Assistance Program ).\n**(B)**\nTitle 28, Code of Federal Regulations, part 23 (commonly known as Justice Information Sharing Training and Technical Assistance Program ).\n**(C)**\nSection 1401 of the Violence Against Women Act Reauthorization Act of 2022 ( 34 U.S.C. 30107 ) to a local law enforcement agency for enforcement of cybercrimes against individuals.\n**(D)**\nSection 1701 title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ), relating to developing and acquiring effective equipment, technologies, and interoperable communications that assist in responding to and preventing crime (commonly known as the COPS Technology and Equipment Program ).\n**(3) General financial fraud**\nThe term general financial fraud means, in order to obtain money or other things of value\u2014\n**(A)**\nintentional misrepresentation of information or identity to deceive an individual;\n**(B)**\nunlawful use of a credit card, debit card, or automated teller machine; or\n**(C)**\nuse of electronic means to transmit deceptive information.\n**(4) Pig butchering**\nThe term pig butchering means a confidence and investment fraud in which the victim is gradually lured into making increasing monetary contributions, generally in the form of cryptocurrency, to a seemingly sound investment before the scammer disappears with the contributed monies.\n**(5) Scam**\nThe term scam means a financial crime undertaken through the use of social engineering that uses deceptive inducement to acquire\u2014\n**(A)**\nauthorized access to funds; or\n**(B)**\npersonal or sensitive information that can facilitate the theft of financial assets.\n**(6) State**\nThe term State means each of the several States, the District of Columbia, and each territory of the United States.\n#### 3. Federal grants used for investigating elder financial fraud, pig butchering, and general financial fraud\n##### (a) In general\nState, local, and Tribal law enforcement agencies and grantees that receive eligible Federal grant funds may use such funds for investigating elder financial fraud, pig butchering, and general financial fraud, including by\u2014\n**(1)**\nhiring and retaining analysts, agents, experts, and other personnel;\n**(2)**\nproviding training specific to complex financial investigations, including training on\u2014\n**(A)**\ncoordination and collaboration between State, local, Tribal, and Federal law enforcement agencies;\n**(B)**\nassisting victims of financial fraud and exploitation;\n**(C)**\nthe use of blockchain intelligence tools and related capabilities relating to emerging technologies identified in the February 2024 Critical and Emerging Technology List Update of the Fast Track Action Subcommittee on Critical and Emerging Technologies of the National Science and Technology Council (the Critical and Emerging Technology List ); and\n**(D)**\nunique aspects of fraud investigations, including transnational financial investigations and emerging technologies identified in the Critical and Emerging Technology List;\n**(3)**\nobtaining software and technical tools to conduct financial fraud and exploitation investigations;\n**(4)**\nencouraging improved data collection and reporting;\n**(5)**\nsupporting training and tabletop exercises to enhance coordination and communication between financial institutions and State, local, Tribal, and Federal law enforcement agencies for the purpose of stopping fraud and scams; and\n**(6)**\ndesignating a financial sector liaison to serve as a point of contact for financial institutions to share and exchange with State, local, Tribal, and Federal law enforcement agencies information relevant to the investigation of fraud and scams.\n##### (b) Report to grant provider\nEach law enforcement agency and grantee that makes use of eligible Federal grant funds for a purpose specified under subsection (a) shall, not later than 1 year after making such use of the funds, submit to the Federal agency that provided the eligible Federal grant funds, a report containing\u2014\n**(1)**\nan explanation of the amount of funds so used, and the specific purpose for which the funds were used;\n**(2)**\nstatistics with respect to elder financial fraud, pig butchering, and general financial fraud in the jurisdiction of the law enforcement agency, along with an analysis of how the use of the funds for a purpose specified under subsection (a) affected such statistics; and\n**(3)**\nan assessment of the ability of the law enforcement agency to deter elder financial fraud, pig butchering, and general financial fraud.\n#### 4. Report on general financial fraud, pig butchering, and elder financial fraud\nNot later than 1 year after the date of enactment of this Act, the Secretary of the Treasury and the Director of the Financial Crimes Enforcement Network in consultation with the Attorney General, the Secretary of Homeland Security, and the appropriate Federal banking agencies and Federal functional regulators shall, jointly, submit to Congress a report on efforts and recommendations related to general financial fraud, pig butchering, elder financial fraud, and scams.\n#### 5. Report on the state of scams in the United States\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Secretary of the Treasury and the Director of the Financial Crimes Enforcement Network, in consultation with the Attorney General, the Secretary of Homeland Security, and the appropriate Federal banking agencies and Federal functional regulators, shall submit a report to Congress on the state of scams in the United States that\u2014\n**(1)**\nestimates\u2014\n**(A)**\nthe number of financial fraud, pig butchering, elder financial fraud, and scams committed against American consumers each year, including\u2014\n**(i)**\nattempted scams, including through social media, online dating services, email, impersonation of financial institutions and nonbank financial institutions; and\n**(ii)**\nsuccessful scams, including through social media, online dating services, email, impersonation of financial institutions and nonbank financial institutions;\n**(B)**\nthe number of consumers each year that lose money to 1 or more scams;\n**(C)**\nthe dollar amount of consumer losses to scams each year;\n**(D)**\nthe percentage of scams each year that can be attributed to\u2014\n**(i)**\noverseas actors; and\n**(ii)**\norganized crime;\n**(E)**\nthe number of attempted scams each year that involve the impersonation of phone numbers associated with financial institutions and nonbank financial institutions; and\n**(F)**\nan estimate of the number of synthetic identities impersonating American consumers each year;\n**(2)**\nprovides an overview of the Federal civil and criminal enforcement actions brought against the recipients of the proceeds of financial fraud, pig butchering, elder financial fraud, and scams during the period covered by the report that includes\u2014\n**(A)**\nthe number of such enforcement actions;\n**(B)**\nan evaluation of the effectiveness of such enforcement actions;\n**(C)**\nan identification of the types of claims brought against the recipients of the proceeds of financial fraud, pig butchering, elder financial fraud, and scams;\n**(D)**\nan identification of the types of penalties imposed through such enforcement actions;\n**(E)**\nan identification of the types of relief obtained through such enforcement actions; and\n**(F)**\nthe number of such enforcement actions that are connected to a Suspicious Activity Report; and\n**(3)**\nidentifies amounts made available and amounts expended to address financial fraud, pig butchering, elder financial fraud, and scams during the period covered by the report by\u2014\n**(A)**\nthe Bureau of Consumer Financial Protection;\n**(B)**\nthe Department of Justice;\n**(C)**\nthe Federal Bureau of Investigation;\n**(D)**\nthe Federal Communications Commission;\n**(E)**\nthe Board of Governors of the Federal Reserve Board;\n**(F)**\nthe Federal Trade Commission;\n**(G)**\nthe Financial Crimes Enforcement Network;\n**(H)**\nthe Securities and Exchange Commission; and\n**(I)**\nthe Social Security Administration.\n##### (b) Solicitation of public comment\nIn carrying out the report required under subsection (a), the Secretary of the Treasury shall solicit comments from consumers, social media companies, email providers, telecommunications companies, financial institutions, and nonbank financial institutions.\n#### 6. Report to Congress\nEach Federal agency that provides eligible Federal grant funds that are used for a purpose specified under section 3(a) shall issue an annual report to the Committee on Banking, Housing, and Urban Affairs of the Senate , the Committee on Financial Services of the House of Representatives , the Committee on the Judiciary of the Senate , and the Committee on the Judiciary of the House of Representatives containing the information received from law enforcement agencies under section 3(b).\n#### 7. Federal law enforcement agencies assisting State, local, and Tribal law enforcement and fusion centers\nFederal law enforcement agencies may assist State, local, and Tribal law enforcement agencies and fusion centers in the use of tracing tools for blockchain and related technology tools.",
      "versionDate": "2025-07-30",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2544rs.xml",
      "text": "II\nCalendar No. 317\n119th CONGRESS\n2d Session\nS. 2544\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mrs. Britt (for herself, Mrs. Gillibrand , Mr. Scott of Florida , Mr. Lankford , Mr. Warnock , Mr. Coons , Ms. Klobuchar , Mrs. Moody , Mr. Grassley , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nFebruary 9, 2026 Reported by Mr. Grassley , without amendment\nA BILL\nTo permit State, local, and Tribal law enforcement agencies and grantees that receive eligible Federal grant funds to use such funds for investigating elder financial fraud, pig butchering, and general financial fraud, and to clarify that Federal law enforcement agencies may assist State, local, and Tribal law enforcement agencies in the use of tracing tools for blockchain and related technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarding Unprotected Aging Retirees from Deception Act or the GUARD Act .\n#### 2. Definitions\nIn this Act:\n**(1) Elder financial fraud**\nThe term elder financial fraud means the illegal or improper use of the money, property, or other resources of an elderly individual or adult with a disability for monetary or personal benefit, profit, or gain.\n**(2) Eligible Federal grant funds**\nThe term eligible Federal grant funds means funds received under any of the following:\n**(A)**\nTitle IV of the Prioritizing Resources and Organization for Intellectual Property Act of 2008 ( 34 U.S.C. 30103 et seq. ) (commonly known as the Economic, High-Technology, White Collar, and Internet Crime Prevention National Training and Technical Assistance Program ), including relating to the use of technology to solve crimes and to facilitate prosecutions (commonly known as the Internet of Things (IoT) National Training and Technical Assistance Program ).\n**(B)**\nTitle 28, Code of Federal Regulations, part 23 (commonly known as Justice Information Sharing Training and Technical Assistance Program ).\n**(C)**\nSection 1401 of the Violence Against Women Act Reauthorization Act of 2022 ( 34 U.S.C. 30107 ) to a local law enforcement agency for enforcement of cybercrimes against individuals.\n**(D)**\nSection 1701 title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ), relating to developing and acquiring effective equipment, technologies, and interoperable communications that assist in responding to and preventing crime (commonly known as the COPS Technology and Equipment Program ).\n**(3) General financial fraud**\nThe term general financial fraud means, in order to obtain money or other things of value\u2014\n**(A)**\nintentional misrepresentation of information or identity to deceive an individual;\n**(B)**\nunlawful use of a credit card, debit card, or automated teller machine; or\n**(C)**\nuse of electronic means to transmit deceptive information.\n**(4) Pig butchering**\nThe term pig butchering means a confidence and investment fraud in which the victim is gradually lured into making increasing monetary contributions, generally in the form of cryptocurrency, to a seemingly sound investment before the scammer disappears with the contributed monies.\n**(5) Scam**\nThe term scam means a financial crime undertaken through the use of social engineering that uses deceptive inducement to acquire\u2014\n**(A)**\nauthorized access to funds; or\n**(B)**\npersonal or sensitive information that can facilitate the theft of financial assets.\n**(6) State**\nThe term State means each of the several States, the District of Columbia, and each territory of the United States.\n#### 3. Federal grants used for investigating elder financial fraud, pig butchering, and general financial fraud\n##### (a) In general\nState, local, and Tribal law enforcement agencies and grantees that receive eligible Federal grant funds may use such funds for investigating elder financial fraud, pig butchering, and general financial fraud, including by\u2014\n**(1)**\nhiring and retaining analysts, agents, experts, and other personnel;\n**(2)**\nproviding training specific to complex financial investigations, including training on\u2014\n**(A)**\ncoordination and collaboration between State, local, Tribal, and Federal law enforcement agencies;\n**(B)**\nassisting victims of financial fraud and exploitation;\n**(C)**\nthe use of blockchain intelligence tools and related capabilities relating to emerging technologies identified in the February 2024 Critical and Emerging Technology List Update of the Fast Track Action Subcommittee on Critical and Emerging Technologies of the National Science and Technology Council (the Critical and Emerging Technology List ); and\n**(D)**\nunique aspects of fraud investigations, including transnational financial investigations and emerging technologies identified in the Critical and Emerging Technology List;\n**(3)**\nobtaining software and technical tools to conduct financial fraud and exploitation investigations;\n**(4)**\nencouraging improved data collection and reporting;\n**(5)**\nsupporting training and tabletop exercises to enhance coordination and communication between financial institutions and State, local, Tribal, and Federal law enforcement agencies for the purpose of stopping fraud and scams; and\n**(6)**\ndesignating a financial sector liaison to serve as a point of contact for financial institutions to share and exchange with State, local, Tribal, and Federal law enforcement agencies information relevant to the investigation of fraud and scams.\n##### (b) Report to grant provider\nEach law enforcement agency and grantee that makes use of eligible Federal grant funds for a purpose specified under subsection (a) shall, not later than 1 year after making such use of the funds, submit to the Federal agency that provided the eligible Federal grant funds, a report containing\u2014\n**(1)**\nan explanation of the amount of funds so used, and the specific purpose for which the funds were used;\n**(2)**\nstatistics with respect to elder financial fraud, pig butchering, and general financial fraud in the jurisdiction of the law enforcement agency, along with an analysis of how the use of the funds for a purpose specified under subsection (a) affected such statistics; and\n**(3)**\nan assessment of the ability of the law enforcement agency to deter elder financial fraud, pig butchering, and general financial fraud.\n#### 4. Report on general financial fraud, pig butchering, and elder financial fraud\nNot later than 1 year after the date of enactment of this Act, the Secretary of the Treasury and the Director of the Financial Crimes Enforcement Network in consultation with the Attorney General, the Secretary of Homeland Security, and the appropriate Federal banking agencies and Federal functional regulators shall, jointly, submit to Congress a report on efforts and recommendations related to general financial fraud, pig butchering, elder financial fraud, and scams.\n#### 5. Report on the state of scams in the United States\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Secretary of the Treasury and the Director of the Financial Crimes Enforcement Network, in consultation with the Attorney General, the Secretary of Homeland Security, and the appropriate Federal banking agencies and Federal functional regulators, shall submit a report to Congress on the state of scams in the United States that\u2014\n**(1)**\nestimates\u2014\n**(A)**\nthe number of financial fraud, pig butchering, elder financial fraud, and scams committed against American consumers each year, including\u2014\n**(i)**\nattempted scams, including through social media, online dating services, email, impersonation of financial institutions and nonbank financial institutions; and\n**(ii)**\nsuccessful scams, including through social media, online dating services, email, impersonation of financial institutions and nonbank financial institutions;\n**(B)**\nthe number of consumers each year that lose money to 1 or more scams;\n**(C)**\nthe dollar amount of consumer losses to scams each year;\n**(D)**\nthe percentage of scams each year that can be attributed to\u2014\n**(i)**\noverseas actors; and\n**(ii)**\norganized crime;\n**(E)**\nthe number of attempted scams each year that involve the impersonation of phone numbers associated with financial institutions and nonbank financial institutions; and\n**(F)**\nan estimate of the number of synthetic identities impersonating American consumers each year;\n**(2)**\nprovides an overview of the Federal civil and criminal enforcement actions brought against the recipients of the proceeds of financial fraud, pig butchering, elder financial fraud, and scams during the period covered by the report that includes\u2014\n**(A)**\nthe number of such enforcement actions;\n**(B)**\nan evaluation of the effectiveness of such enforcement actions;\n**(C)**\nan identification of the types of claims brought against the recipients of the proceeds of financial fraud, pig butchering, elder financial fraud, and scams;\n**(D)**\nan identification of the types of penalties imposed through such enforcement actions;\n**(E)**\nan identification of the types of relief obtained through such enforcement actions; and\n**(F)**\nthe number of such enforcement actions that are connected to a Suspicious Activity Report; and\n**(3)**\nidentifies amounts made available and amounts expended to address financial fraud, pig butchering, elder financial fraud, and scams during the period covered by the report by\u2014\n**(A)**\nthe Bureau of Consumer Financial Protection;\n**(B)**\nthe Department of Justice;\n**(C)**\nthe Federal Bureau of Investigation;\n**(D)**\nthe Federal Communications Commission;\n**(E)**\nthe Board of Governors of the Federal Reserve Board;\n**(F)**\nthe Federal Trade Commission;\n**(G)**\nthe Financial Crimes Enforcement Network;\n**(H)**\nthe Securities and Exchange Commission; and\n**(I)**\nthe Social Security Administration.\n##### (b) Solicitation of public comment\nIn carrying out the report required under subsection (a), the Secretary of the Treasury shall solicit comments from consumers, social media companies, email providers, telecommunications companies, financial institutions, and nonbank financial institutions.\n#### 6. Report to Congress\nEach Federal agency that provides eligible Federal grant funds that are used for a purpose specified under section 3(a) shall issue an annual report to the Committee on Banking, Housing, and Urban Affairs of the Senate , the Committee on Financial Services of the House of Representatives , the Committee on the Judiciary of the Senate , and the Committee on the Judiciary of the House of Representatives containing the information received from law enforcement agencies under section 3(b).\n#### 7. Federal law enforcement agencies assisting State, local, and Tribal law enforcement and fusion centers\nFederal law enforcement agencies may assist State, local, and Tribal law enforcement agencies and fusion centers in the use of tracing tools for blockchain and related technology tools.",
      "versionDate": "2025-07-30",
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
        "actionDate": "2025-04-21",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2978",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GUARD Act",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-03-16T18:54:44Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-16T18:55:02Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2026-03-16T18:54:05Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2026-03-16T18:54:50Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2026-03-16T18:53:54Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-03-16T18:54:00Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-03-16T18:53:43Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-16T18:54:56Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-03-16T18:53:49Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2026-03-16T18:53:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-16T15:28:58Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2544is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2544rs.xml"
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
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-11T06:23:20Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Guarding Unprotected Aging Retirees from Deception Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-11T06:23:20Z"
    },
    {
      "title": "GUARD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guarding Unprotected Aging Retirees from Deception Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to permit State, local, and Tribal law enforcement agencies and grantees that receive eligible Federal grant funds to use such funds for investigating elder financial fraud, pig butchering, and general financial fraud, and to clarify that Federal law enforcement agencies may assist State, local, and Tribal law enforcement agencies in the use of tracing tools for blockchain and related technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:23Z"
    }
  ]
}
```
