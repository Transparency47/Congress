# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2680?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2680
- Title: LETITIA Act
- Congress: 119
- Bill type: S
- Bill number: 2680
- Origin chamber: Senate
- Introduced date: 2025-08-02
- Update date: 2025-09-18T20:05:48Z
- Update date including text: 2025-09-18T20:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-02: Introduced in Senate
- 2025-08-02 - IntroReferral: Introduced in Senate
- 2025-08-02 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-08-02: Introduced in Senate

## Actions

- 2025-08-02 - IntroReferral: Introduced in Senate
- 2025-08-02 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-02",
    "latestAction": {
      "actionDate": "2025-08-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2680",
    "number": "2680",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "LETITIA Act",
    "type": "S",
    "updateDate": "2025-09-18T20:05:48Z",
    "updateDateIncludingText": "2025-09-18T20:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-02",
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
      "actionDate": "2025-08-02",
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
          "date": "2025-08-02T15:38:21Z",
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
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-08-02",
      "state": "NE"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-08-02",
      "state": "MS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-08-02",
      "state": "NC"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-08-02",
      "state": "LA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-08-02",
      "state": "NE"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-08-02",
      "state": "MT"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2680is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2680\nIN THE SENATE OF THE UNITED STATES\nAugust 2, 2025 Mr. Cornyn (for himself, Mrs. Fischer , Mr. Wicker , Mr. Budd , Mr. Kennedy , Mr. Ricketts , and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish sentencing enhancements for offenses relating to bank, mortgage, credit, and tax fraud committed by elected public officials, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Law Enforcement Tools to Interdict Troubling Investments in Abodes Act or the LETITIA Act .\n#### 2. Findings\nIt is the sense of Congress that:\n**(1)**\nIn the United States, citizens elect civic and political leaders to represent their interests and act on their behalf.\n**(2)**\nIn return for being given this sacred trust, public officials are expected to fully adhere to the highest ethical and moral standards, and must discharge their duties faithfully, honestly, and impartially, free from any personal considerations or gain.\n**(3)**\nPublic service is a public trust, and the Government only functions when there is trust between the electorate and public officials.\n**(4)**\nWhen public officials abuse the faith that citizens place in them by committing crimes of dishonesty or moral turpitude, they betray both their office and the public, and deserve heightened punishment.\n**(5)**\nFraud is, at its core, a crime of dishonesty.\n**(6)**\nMortgage, bank, credit, and tax frauds require deception and lies, and harm the victim financial institutions, investors, and the broader public.\n**(7)**\nTherefore, public officials who commit these crimes deserve punishments above and beyond what a normal citizen should receive.\n**(8)**\nSuch punishment must include mandatory minimum sentences of imprisonment for any public official to ensure that they cannot abuse their positions of influence to cut sweetheart or backroom deals that the average citizen would be unable to make.\n**(9)**\nIf a public official commits multiple frauds, demonstrating a pattern and practice of dishonest, unethical, and illegal behavior, justice demands that the public official should face even harsher mandatory penalties.\n**(10)**\nNo person is above the law, and public officials who commit fraud must be held to account. Integrity matters.\n#### 3. Enhanced penalties for public officials who commit bank fraud\nSection 1344 of title 18, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking Whoever knowingly executes, or attempts to execute, and inserting the following:\n(a) Offense It shall be unlawful to knowingly execute, or attempt to execute, ;\n**(2)**\nin subsection (a)(2), as so designated by paragraph (1), by striking the semicolon at the end and inserting a period;\n**(3)**\nby striking shall be fined not more than $1,000,000 or imprisoned not more than 30 years, or both. ; and\n**(4)**\nby adding at the end the following:\n(b) Penalty (1) In general Except as provided in paragraph (2), a person convicted of a violation of subsection (a) shall be fined not more than $1,000,000, imprisoned not more than 30 years, or both. (2) Public official (A) Definition In this paragraph, the term public official means an officer, employee, elected or appointed representative of, or an individual acting for or on behalf of, the United States, a State, or a subdivision of a State, or any department, agency, or branch of government, in any official function, under or by the authority of any such department, agency, or branch of government. (B) Enhanced penalties In the case of an individual who is a public official at the time of an offense described in subsection (a)\u2014 (i) if the offense is the first or second such offense, the individual shall be fined not more than $1,500,000 and imprisoned not less than 1 year and not more than 35 years; and (ii) if the offense is the third or subsequent such offense, the individual shall be fined not more than $2,000,000 and imprisoned not less than 5 years and not more than 40 years. .\n#### 4. Enhanced penalties for public officials who falsify loan and credit applications\nSection 1014 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever knowingly and inserting:\n(a) Offense Whoever knowingly ;\n**(2)**\nby striking shall and all that follows, and inserting shall be punished as provided in subsection (b). ; and\n**(3)**\nby adding at the end the following:\n(b) Penalty (1) In general Except as provided in paragraph (2), a person convicted of a violation of subsection (a) shall be fined not more than $1,000,000, imprisoned not more than 30 years, or both. (2) Public officials In the case of an individual who is a public official at the time of an offense described in subsection (a)\u2014 (A) if the offense is the first or second such offense, the individual shall be fined not more than $1,500,000 and imprisoned not less than 1 year and not more than 35 years; and (B) if the offense is the third or subsequent such offense, the individual shall be fined not more than $2,000,000 and imprisoned not less than 5 years and not more than 40 years. (c) Definitions In this section: (1) Public official The term public official means an officer, employee, elected or appointed representative of, or an individual acting for or on behalf of, the United States, a State, or a subdivision of a State, or any department, agency, or branch of government, in any official function, under or by the authority of any such department, agency, or branch of government. (2) State-chartered credit union The term State-chartered credit union includes a credit union chartered under the laws of a State of the United States, the District of Columbia, or any commonwealth, territory, or possession of the United States. .\n#### 5. Enhanced penalties for public officials who falsify tax filings\nSection 7206 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking Any person and inserting the following:\n(a) In general Any person , and\n**(2)**\nby adding at the end the following new subsection:\n(b) Enhanced penalty for public officials (1) In general In the case of an individual who is a public official at the time of an offense described in subsection (a)\u2014 (A) if the offense is the first or second such offense, subsection (a) shall be applied\u2014 (i) by substituting $150,000 for $100,000 , and (ii) by substituting not less than 6 months and not more than 5 years for not more than 3 years , and (B) if the offense is the third or subsequent such offence, subsection (a) shall be applied\u2014 (i) by substituting $200,000 for $100,000 , and (ii) by substituting not less than 2 years and not more than 10 years for not more than 3 years . (2) Public official For purposes of this subsection, the term public official means an officer, employee, elected or appointed representative of, or an individual acting for or on behalf of, the United States, a State, or a subdivision of a State, or any department, agency, or branch of government, in any official function, under or by the authority of any such department, agency, or branch of government. .\n#### 6. Public integrity enforcement guidance for the department of justice and the department of the treasury\n##### (a) Directive to Department of Justice Law Enforcement Officials and Task Forces\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Attorney General shall issue a directive to\u2014\n**(A)**\nall Federal law enforcement officers and relevant personnel employed by the Department of Justice who may be involved in the investigation of bank fraud and falsification of loan and credit applications; and\n**(B)**\nmembers of all task forces led by the Department of Justice or a component thereof that participate in the investigation of bank fraud and falsification of loan and credit applications.\n**(2) Required instructions**\nThe directive required to be issued under paragraph (1) shall include instructions on\u2014\n**(A)**\nthe updates made by this Act to sections 1014 and 1344 of title 18, United States Code; and\n**(B)**\nthe investigation of public officials who commit bank fraud and falsification of loan and credit applications and how such individuals should be investigated for such acts.\n##### (b) Directive to Department of Treasury Officials\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Secretary of the Treasury, in consultation with the Attorney General, shall issue a directive to\u2014\n**(A)**\nall Federal law enforcement officers and relevant personnel employed by the Department of the Treasury who may be involved in the investigation of falsified tax filings; and\n**(B)**\nmembers of all task forces led by the Department of the Treasury or a component thereof that participate in the investigation of falsified tax filings.\n**(2) Required instructions**\nThe directive required to be issued under paragraph (1) shall include instructions on\u2014\n**(A)**\nthe updates made by this Act to section 7206 of the Internal Revenue Code of 1986;\n**(B)**\nthe investigation of public officials who falsify tax filings and how such individuals should be investigated for such acts; and\n**(C)**\nbest practices for collaborating with the Department of Justice and components thereof in the investigation and prosecution of public officials who falsify tax filings.\n#### 7. Effective date\nThe amendments made by this Act shall apply to convictions after the date of enactment of this Act.",
      "versionDate": "2025-08-02",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-18T20:05:48Z"
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
      "date": "2025-08-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2680is.xml"
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
      "title": "LETITIA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LETITIA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Law Enforcement Tools to Interdict Troubling Investments in Abodes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish sentencing enhancements for offenses relating to bank, mortgage, credit, and tax fraud committed by elected public officials, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:03:19Z"
    }
  ]
}
```
