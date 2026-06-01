# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3966?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3966
- Title: TREY'S Law
- Congress: 119
- Bill type: S
- Bill number: 3966
- Origin chamber: Senate
- Introduced date: 2026-03-03
- Update date: 2026-05-26T18:45:49Z
- Update date including text: 2026-05-26T18:45:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in Senate
- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 413.
- 2026-05-20 - Floor: Message on Senate action sent to the House.
- 2026-05-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2398-2400; text: CR S2399-2400)
- 2026-05-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-05-20 16:30:23 - Floor: Received in the House.
- 2026-05-20 16:38:55 - Floor: Held at the desk.
- Latest action: 2026-03-03: Introduced in Senate

## Actions

- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 413.
- 2026-05-20 - Floor: Message on Senate action sent to the House.
- 2026-05-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2398-2400; text: CR S2399-2400)
- 2026-05-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-05-20 16:30:23 - Floor: Received in the House.
- 2026-05-20 16:38:55 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3966",
    "number": "3966",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "TREY'S Law",
    "type": "S",
    "updateDate": "2026-05-26T18:45:49Z",
    "updateDateIncludingText": "2026-05-26T18:45:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-05-20",
      "actionTime": "16:38:55",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-05-20",
      "actionTime": "16:30:23",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S2398-2400; text: CR S2399-2400)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 413.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-19",
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
      "actionDate": "2026-05-19",
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
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
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
            "date": "2026-05-19T18:47:19Z",
            "name": "Reported By"
          },
          {
            "date": "2026-05-14T17:58:14Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-03T16:02:07Z",
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
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MO"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "VT"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NH"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MN"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "MO"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TN"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "IL"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "SC"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "FL"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "NC"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "LA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "DE"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "NJ"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3966is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3966\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2026 Mr. Cruz (for himself, Mrs. Gillibrand , Mrs. Britt , Mr. Schmitt , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit the enforcement of certain contractual clauses that restrict disclosure of sexual abuse of minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Terminating Restrictive Enforcement of Youth Settlements Law or TREY'S Law .\n#### 2. Findings and purposes\n##### (a) Findings\n**(1) Instrumentalities of interstate commerce**\nCongress finds the following:\n**(A)**\nSexual abuse of minors, including abuse facilitated through instrumentalities of interstate commerce, is a matter of national concern.\n**(B)**\nAgreements containing nondisclosure and confidentiality provisions, frequently concluded through the instrumentalities of interstate commerce, have been used to silence survivors of sexual abuse and conceal ongoing or repeated abuse.\n**(C)**\nThe enforcement of such provisions interferes with reporting to law enforcement agencies, child protection authorities, Federal regulators, Members of Congress, and the courts, and frustrates the enforcement of Federal criminal and civil law.\n**(2) Necessary and proper clause and enforcement of Federal criminal law**\nCongress further finds the following:\n**(A)**\nSexual abuse and trafficking of minors are prohibited under Federal criminal law, including chapter 110 of title 18, United States Code, and section 1591 of title 18, United States Code.\n**(B)**\nNondisclosure and confidentiality agreements that prohibit or restrict disclosure of sexual abuse of a minor interfere with reporting to law enforcement, child protection authorities, courts, Federal regulators, and Members of Congress.\n**(C)**\nSuch agreements frustrate the investigation and prosecution of Federal crimes, chill cooperation with law enforcement, and function as private mechanisms to obstruct justice.\n**(D)**\nCongress has authority under clause 18 of section 8 of article I of the Constitution of the United States (commonly known as the Necessary and Proper Clause ) to ensure that private agreements are not used to impede the enforcement of Federal criminal and civil law protecting minors from sexual exploitation and abuse.\n**(3) State action and section 5 of the 14th Amendment**\nCongress further finds the following:\n**(A)**\nSurvivors of child sexual abuse possess fundamental constitutional interests, secured by provisions of the Bill of Rights as incorporated against the States through the 14th Amendment to the Constitution of the United States, in reporting crimes, seeking redress through the courts, cooperating with law enforcement, and petitioning the government for protection and enforcement.\n**(B)**\nWhen State courts or other governmental authorities enforce nondisclosure or confidentiality provisions that prohibit or restrict disclosure of sexual abuse of a minor, such enforcement constitutes State action for purposes of the 14th Amendment to the Constitution of the United States.\n**(C)**\nJudicial enforcement of such provisions may deprive survivors of due process of law, equal protection of the laws, and meaningful access to courts, including rights derived from the First Amendment to the Constitution of the United States and incorporated against the States, in violation of the 14th Amendment.\n**(D)**\nAgreements that obstruct justice, suppress the reporting of crimes, or conceal criminal conduct have long been regarded at common law, including at the time of the founding of the United States, as void and unenforceable as against public policy, and fall outside the traditional scope of protected contractual liberty.\n**(E)**\nAt the time of the founding of the United States, private agreements purporting to suppress prosecution, conceal felonies, or restrain the reporting of crimes were not recognized as valid or enforceable contracts, and no party possessed a vested right in their judicial enforcement.\n**(F)**\nCongress has authority under section 5 of the 14th Amendment to the Constitution of the United States to enact appropriate remedial and preventive legislation to prevent and remedy constitutional violations arising from State judicial enforcement of private agreements that suppress disclosure of criminal conduct involving minors.\n##### (b) Purpose\nThe purpose of this Act is\u2014\n**(1)**\nto enforce the guarantees of the 14th Amendment to the Constitution of the United States, including the right to petition the government for redress of grievances and the right of access to courts, by preventing State courts and other governmental authorities from enforcing nondisclosure or confidentiality provisions that suppress disclosure of sexual abuse of minors;\n**(2)**\nto ensure, pursuant to the authority of Congress under article I of the Constitution of the United States, including the Necessary and Proper Clause, that private agreements are not used to obstruct the investigation or prosecution of Federal crimes involving the sexual abuse or trafficking of minors;\n**(3)**\nto preserve access to courts and the right to petition the government for redress of grievances; and\n**(4)**\nto ensure that survivors of sexual abuse of minors, and persons with knowledge of such abuse, may disclose such abuse freely and without fear of civil liability.\n#### 3. Definitions\nIn this Act:\n**(1) Minor person**\nThe term minor person means an individual who has not attained 18 years of age.\n**(2) Nondisclosure clause**\nThe term nondisclosure clause means a provision in a contract or agreement that prohibits 1 or more parties to the contract or agreement from disclosing conduct or information covered by the terms and conditions of the contract or agreement.\n**(3) Sexual abuse against a minor person**\nThe term sexual abuse against a minor person means\u2014\n**(A)**\nconduct that constitutes or allegedly constitutes\u2014\n**(i)**\nan offense under chapter 110 of title 18, United States Code; or\n**(ii)**\nsex trafficking of a minor person under section 1591 of title 18, United States Code; or\n**(B)**\nany sexual act or sexual contact involving a minor person that constitutes a criminal offense under Federal law or the law of the State in which the act or contact occurs.\n#### 4. Nondisclosure agreements void and unenforceable\n##### (a) In general\nA nondisclosure clause shall be void and unenforceable as against public policy only to the extent that the nondisclosure clause prohibits\u2014\n**(1)**\na victim or alleged victim of sexual abuse against a minor person from disclosing\u2014\n**(A)**\nthat act of sexual abuse against a minor person; or\n**(B)**\nfacts related to that act of sexual abuse against a minor person; or\n**(2)**\nany other person from disclosing facts related to sexual abuse against a minor person described in paragraph (1) in support of, in furtherance of, or consistent with the right of a victim or alleged victim to disclose under that paragraph.\n##### (b) Permissible confidentiality\nNothing in this section shall be construed to prohibit a person, including a victim or alleged victim of sexual abuse against a minor person, from entering into a contract or agreement that restricts the disclosure of information, including the amount or payment terms of a settlement, by another party to the contract or agreement, including an alleged perpetrator, so long as such restriction does not prevent disclosure protected under subsection (a).\n#### 5. Retroactive application\n##### (a) In general\nThis Act shall apply to any nondisclosure clause in a contract or agreement entered into before, on, or after the date of enactment of this Act.\n##### (b) No enforcement actions\nNo person may enforce or attempt to enforce a nondisclosure clause described in section 4(a), regardless of the date on which the contract or agreement containing the nondisclosure clause was entered into.\n##### (c) Preemption\n**(1) In general**\nThis Act supersedes any State law to the extent that such law permits enforcement of a provision, the enforcement of which is prohibited under this Act.\n**(2) Rule of construction**\nNothing in this Act shall be construed to prohibit a State or locality from enacting legislation that\u2014\n**(A)**\nis consistent with this Act; or\n**(B)**\nprovides greater protection to a victim of sexual abuse against a minor person than is provided under this Act.",
      "versionDate": "2026-03-03",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3966rs.xml",
      "text": "II\nCalendar No. 413\n119th CONGRESS\n2d Session\nS. 3966\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2026 Mr. Cruz (for himself, Mrs. Gillibrand , Mrs. Britt , Mr. Schmitt , Mr. Welch , Mrs. Shaheen , Mr. Cornyn , Ms. Klobuchar , Mr. Hawley , Mrs. Blackburn , Mr. Durbin , Mr. Graham , Mrs. Moody , Mr. Tillis , Mr. Kennedy , Mr. Coons , Ms. Hirono , Mr. Blumenthal , Mr. Padilla , Mr. Booker , and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 19, 2026 Reported by Mr. Grassley , without amendment\nA BILL\nTo prohibit the enforcement of certain contractual clauses that restrict disclosure of sexual abuse of minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Terminating Restrictive Enforcement of Youth Settlements Law or TREY'S Law .\n#### 2. Findings and purposes\n##### (a) Findings\n**(1) Instrumentalities of interstate commerce**\nCongress finds the following:\n**(A)**\nSexual abuse of minors, including abuse facilitated through instrumentalities of interstate commerce, is a matter of national concern.\n**(B)**\nAgreements containing nondisclosure and confidentiality provisions, frequently concluded through the instrumentalities of interstate commerce, have been used to silence survivors of sexual abuse and conceal ongoing or repeated abuse.\n**(C)**\nThe enforcement of such provisions interferes with reporting to law enforcement agencies, child protection authorities, Federal regulators, Members of Congress, and the courts, and frustrates the enforcement of Federal criminal and civil law.\n**(2) Necessary and proper clause and enforcement of Federal criminal law**\nCongress further finds the following:\n**(A)**\nSexual abuse and trafficking of minors are prohibited under Federal criminal law, including chapter 110 of title 18, United States Code, and section 1591 of title 18, United States Code.\n**(B)**\nNondisclosure and confidentiality agreements that prohibit or restrict disclosure of sexual abuse of a minor interfere with reporting to law enforcement, child protection authorities, courts, Federal regulators, and Members of Congress.\n**(C)**\nSuch agreements frustrate the investigation and prosecution of Federal crimes, chill cooperation with law enforcement, and function as private mechanisms to obstruct justice.\n**(D)**\nCongress has authority under clause 18 of section 8 of article I of the Constitution of the United States (commonly known as the Necessary and Proper Clause ) to ensure that private agreements are not used to impede the enforcement of Federal criminal and civil law protecting minors from sexual exploitation and abuse.\n**(3) State action and section 5 of the 14th Amendment**\nCongress further finds the following:\n**(A)**\nSurvivors of child sexual abuse possess fundamental constitutional interests, secured by provisions of the Bill of Rights as incorporated against the States through the 14th Amendment to the Constitution of the United States, in reporting crimes, seeking redress through the courts, cooperating with law enforcement, and petitioning the government for protection and enforcement.\n**(B)**\nWhen State courts or other governmental authorities enforce nondisclosure or confidentiality provisions that prohibit or restrict disclosure of sexual abuse of a minor, such enforcement constitutes State action for purposes of the 14th Amendment to the Constitution of the United States.\n**(C)**\nJudicial enforcement of such provisions may deprive survivors of due process of law, equal protection of the laws, and meaningful access to courts, including rights derived from the First Amendment to the Constitution of the United States and incorporated against the States, in violation of the 14th Amendment.\n**(D)**\nAgreements that obstruct justice, suppress the reporting of crimes, or conceal criminal conduct have long been regarded at common law, including at the time of the founding of the United States, as void and unenforceable as against public policy, and fall outside the traditional scope of protected contractual liberty.\n**(E)**\nAt the time of the founding of the United States, private agreements purporting to suppress prosecution, conceal felonies, or restrain the reporting of crimes were not recognized as valid or enforceable contracts, and no party possessed a vested right in their judicial enforcement.\n**(F)**\nCongress has authority under section 5 of the 14th Amendment to the Constitution of the United States to enact appropriate remedial and preventive legislation to prevent and remedy constitutional violations arising from State judicial enforcement of private agreements that suppress disclosure of criminal conduct involving minors.\n##### (b) Purpose\nThe purpose of this Act is\u2014\n**(1)**\nto enforce the guarantees of the 14th Amendment to the Constitution of the United States, including the right to petition the government for redress of grievances and the right of access to courts, by preventing State courts and other governmental authorities from enforcing nondisclosure or confidentiality provisions that suppress disclosure of sexual abuse of minors;\n**(2)**\nto ensure, pursuant to the authority of Congress under article I of the Constitution of the United States, including the Necessary and Proper Clause, that private agreements are not used to obstruct the investigation or prosecution of Federal crimes involving the sexual abuse or trafficking of minors;\n**(3)**\nto preserve access to courts and the right to petition the government for redress of grievances; and\n**(4)**\nto ensure that survivors of sexual abuse of minors, and persons with knowledge of such abuse, may disclose such abuse freely and without fear of civil liability.\n#### 3. Definitions\nIn this Act:\n**(1) Minor person**\nThe term minor person means an individual who has not attained 18 years of age.\n**(2) Nondisclosure clause**\nThe term nondisclosure clause means a provision in a contract or agreement that prohibits 1 or more parties to the contract or agreement from disclosing conduct or information covered by the terms and conditions of the contract or agreement.\n**(3) Sexual abuse against a minor person**\nThe term sexual abuse against a minor person means\u2014\n**(A)**\nconduct that constitutes or allegedly constitutes\u2014\n**(i)**\nan offense under chapter 110 of title 18, United States Code; or\n**(ii)**\nsex trafficking of a minor person under section 1591 of title 18, United States Code; or\n**(B)**\nany sexual act or sexual contact involving a minor person that constitutes a criminal offense under Federal law or the law of the State in which the act or contact occurs.\n#### 4. Nondisclosure agreements void and unenforceable\n##### (a) In general\nA nondisclosure clause shall be void and unenforceable as against public policy only to the extent that the nondisclosure clause prohibits\u2014\n**(1)**\na victim or alleged victim of sexual abuse against a minor person from disclosing\u2014\n**(A)**\nthat act of sexual abuse against a minor person; or\n**(B)**\nfacts related to that act of sexual abuse against a minor person; or\n**(2)**\nany other person from disclosing facts related to sexual abuse against a minor person described in paragraph (1) in support of, in furtherance of, or consistent with the right of a victim or alleged victim to disclose under that paragraph.\n##### (b) Permissible confidentiality\nNothing in this section shall be construed to prohibit a person, including a victim or alleged victim of sexual abuse against a minor person, from entering into a contract or agreement that restricts the disclosure of information, including the amount or payment terms of a settlement, by another party to the contract or agreement, including an alleged perpetrator, so long as such restriction does not prevent disclosure protected under subsection (a).\n#### 5. Retroactive application\n##### (a) In general\nThis Act shall apply to any nondisclosure clause in a contract or agreement entered into before, on, or after the date of enactment of this Act.\n##### (b) No enforcement actions\nNo person may enforce or attempt to enforce a nondisclosure clause described in section 4(a), regardless of the date on which the contract or agreement containing the nondisclosure clause was entered into.\n##### (c) Preemption\n**(1) In general**\nThis Act supersedes any State law to the extent that such law permits enforcement of a provision, the enforcement of which is prohibited under this Act.\n**(2) Rule of construction**\nNothing in this Act shall be construed to prohibit a State or locality from enacting legislation that\u2014\n**(A)**\nis consistent with this Act; or\n**(B)**\nprovides greater protection to a victim of sexual abuse against a minor person than is provided under this Act.",
      "versionDate": "2026-05-19",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3966es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 3966\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo prohibit the enforcement of certain contractual clauses that restrict disclosure of sexual abuse of minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Terminating Restrictive Enforcement of Youth Settlements Law or TREY'S Law .\n#### 2. Findings and purposes\n##### (a) Findings\n**(1) Instrumentalities of interstate commerce**\nCongress finds the following:\n**(A)**\nSexual abuse of minors, including abuse facilitated through instrumentalities of interstate commerce, is a matter of national concern.\n**(B)**\nAgreements containing nondisclosure and confidentiality provisions, frequently concluded through the instrumentalities of interstate commerce, have been used to silence survivors of sexual abuse and conceal ongoing or repeated abuse.\n**(C)**\nThe enforcement of such provisions interferes with reporting to law enforcement agencies, child protection authorities, Federal regulators, Members of Congress, and the courts, and frustrates the enforcement of Federal criminal and civil law.\n**(2) Necessary and proper clause and enforcement of Federal criminal law**\nCongress further finds the following:\n**(A)**\nSexual abuse and trafficking of minors are prohibited under Federal criminal law, including chapter 110 of title 18, United States Code, and section 1591 of title 18, United States Code.\n**(B)**\nNondisclosure and confidentiality agreements that prohibit or restrict disclosure of sexual abuse of a minor interfere with reporting to law enforcement, child protection authorities, courts, Federal regulators, and Members of Congress.\n**(C)**\nSuch agreements frustrate the investigation and prosecution of Federal crimes, chill cooperation with law enforcement, and function as private mechanisms to obstruct justice.\n**(D)**\nCongress has authority under clause 18 of section 8 of article I of the Constitution of the United States (commonly known as the Necessary and Proper Clause ) to ensure that private agreements are not used to impede the enforcement of Federal criminal and civil law protecting minors from sexual exploitation and abuse.\n**(3) State action and section 5 of the 14th Amendment**\nCongress further finds the following:\n**(A)**\nSurvivors of child sexual abuse possess fundamental constitutional interests, secured by provisions of the Bill of Rights as incorporated against the States through the 14th Amendment to the Constitution of the United States, in reporting crimes, seeking redress through the courts, cooperating with law enforcement, and petitioning the government for protection and enforcement.\n**(B)**\nWhen State courts or other governmental authorities enforce nondisclosure or confidentiality provisions that prohibit or restrict disclosure of sexual abuse of a minor, such enforcement constitutes State action for purposes of the 14th Amendment to the Constitution of the United States.\n**(C)**\nJudicial enforcement of such provisions may deprive survivors of due process of law, equal protection of the laws, and meaningful access to courts, including rights derived from the First Amendment to the Constitution of the United States and incorporated against the States, in violation of the 14th Amendment.\n**(D)**\nAgreements that obstruct justice, suppress the reporting of crimes, or conceal criminal conduct have long been regarded at common law, including at the time of the founding of the United States, as void and unenforceable as against public policy, and fall outside the traditional scope of protected contractual liberty.\n**(E)**\nAt the time of the founding of the United States, private agreements purporting to suppress prosecution, conceal felonies, or restrain the reporting of crimes were not recognized as valid or enforceable contracts, and no party possessed a vested right in their judicial enforcement.\n**(F)**\nCongress has authority under section 5 of the 14th Amendment to the Constitution of the United States to enact appropriate remedial and preventive legislation to prevent and remedy constitutional violations arising from State judicial enforcement of private agreements that suppress disclosure of criminal conduct involving minors.\n##### (b) Purpose\nThe purpose of this Act is\u2014\n**(1)**\nto enforce the guarantees of the 14th Amendment to the Constitution of the United States, including the right to petition the government for redress of grievances and the right of access to courts, by preventing State courts and other governmental authorities from enforcing nondisclosure or confidentiality provisions that suppress disclosure of sexual abuse of minors;\n**(2)**\nto ensure, pursuant to the authority of Congress under article I of the Constitution of the United States, including the Necessary and Proper Clause, that private agreements are not used to obstruct the investigation or prosecution of Federal crimes involving the sexual abuse or trafficking of minors;\n**(3)**\nto preserve access to courts and the right to petition the government for redress of grievances; and\n**(4)**\nto ensure that survivors of sexual abuse of minors, and persons with knowledge of such abuse, may disclose such abuse freely and without fear of civil liability.\n#### 3. Definitions\nIn this Act:\n**(1) Minor person**\nThe term minor person means an individual who has not attained 18 years of age.\n**(2) Nondisclosure clause**\nThe term nondisclosure clause means a provision in a contract or agreement that prohibits 1 or more parties to the contract or agreement from disclosing conduct or information covered by the terms and conditions of the contract or agreement.\n**(3) Sexual abuse against a minor person**\nThe term sexual abuse against a minor person means\u2014\n**(A)**\nconduct that constitutes or allegedly constitutes\u2014\n**(i)**\nan offense under chapter 110 of title 18, United States Code; or\n**(ii)**\nsex trafficking of a minor person under section 1591 of title 18, United States Code; or\n**(B)**\nany sexual act or sexual contact involving a minor person that constitutes a criminal offense under Federal law or the law of the State in which the act or contact occurs.\n#### 4. Nondisclosure agreements void and unenforceable\n##### (a) In general\nA nondisclosure clause shall be void and unenforceable as against public policy only to the extent that the nondisclosure clause prohibits\u2014\n**(1)**\na victim or alleged victim of sexual abuse against a minor person from disclosing\u2014\n**(A)**\nthat act of sexual abuse against a minor person; or\n**(B)**\nfacts related to that act of sexual abuse against a minor person; or\n**(2)**\nany other person from disclosing facts related to sexual abuse against a minor person described in paragraph (1) in support of, in furtherance of, or consistent with the right of a victim or alleged victim to disclose under that paragraph.\n##### (b) Permissible confidentiality\nNothing in this section shall be construed to prohibit a person, including a victim or alleged victim of sexual abuse against a minor person, from entering into a contract or agreement that restricts the disclosure of information, including the amount or payment terms of a settlement, by another party to the contract or agreement, including an alleged perpetrator, so long as such restriction does not prevent disclosure protected under subsection (a).\n#### 5. Retroactive application\n##### (a) In general\nThis Act shall apply to any nondisclosure clause in a contract or agreement entered into before, on, or after the date of enactment of this Act.\n##### (b) No enforcement actions\nNo person may enforce or attempt to enforce a nondisclosure clause described in section 4(a), regardless of the date on which the contract or agreement containing the nondisclosure clause was entered into.\n##### (c) Preemption\n**(1) In general**\nThis Act supersedes any State law to the extent that such law permits enforcement of a provision, the enforcement of which is prohibited under this Act.\n**(2) Rule of construction**\nNothing in this Act shall be construed to prohibit a State or locality from enacting legislation that\u2014\n**(A)**\nis consistent with this Act; or\n**(B)**\nprovides greater protection to a victim of sexual abuse against a minor person than is provided under this Act.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2026-04-29",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "8571",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TREY'S Law",
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
        "name": "Law",
        "updateDate": "2026-04-06T12:44:03Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3966is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3966rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3966es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "TREY'S Law",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-05-22T02:38:26Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Terminating Restrictive Enforcement of Youth Settlements Law",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-05-22T02:38:26Z"
    },
    {
      "title": "TREY'S Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "TREY'S Law",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-20T14:38:31Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Terminating Restrictive Enforcement of Youth Settlements Law",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-20T14:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TREY'S Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Terminating Restrictive Enforcement of Youth Settlements Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the enforcement of certain contractual clauses that restrict disclosure of sexual abuse of minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T03:18:25Z"
    }
  ]
}
```
