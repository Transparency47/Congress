# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4316?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4316
- Title: Sanctuary City Elimination Act
- Congress: 119
- Bill type: S
- Bill number: 4316
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-05-13T17:36:49Z
- Update date including text: 2026-05-13T17:36:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-16: Introduced in Senate

## Actions

- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4316",
    "number": "4316",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
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
    "title": "Sanctuary City Elimination Act",
    "type": "S",
    "updateDate": "2026-05-13T17:36:49Z",
    "updateDateIncludingText": "2026-05-13T17:36:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T16:33:33Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "WY"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "WY"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "ND"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "MO"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4316is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4316\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Cornyn (for himself, Mr. Budd , Mr. Barrasso , Mr. Scott of South Carolina , Ms. Lummis , Mr. Cramer , and Mr. Schmitt ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo ensure that State and local law enforcement may cooperate with Federal officials to protect our communities from violent criminals and suspected terrorists who are illegally present in the United States.\n#### 1. Short title\nThis Act may be cited as the Sanctuary City Elimination Act .\n#### 2. Ensuring that local and Federal law enforcement officers may cooperate to safeguard our communities\n##### (a) Authority To cooperate with Federal officials\nA State, a political subdivision of a State, or an officer, employee, or agent of such State or political subdivision that complies with a detainer issued by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act (8 U.S.C. 1226 and 1357)\u2014\n**(1)**\nshall be deemed to be acting as an agent of the Department of Homeland Security; and\n**(2)**\nwith regard to actions taken to comply with the detainer, shall have all authority available to officers and employees of the Department of Homeland Security.\n##### (b) Legal proceedings\nIn any legal proceeding brought against a State, a political subdivision of a State, or an officer, employee, or agent of such State or political subdivision, which challenges the legality of the seizure or detention of an individual pursuant to a detainer issued by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act (8 U.S.C. 1226 and 1357)\u2014\n**(1)**\nno liability shall lie against the State or political subdivision of a State for actions taken in compliance with the detainer; and\n**(2)**\nif the actions of the officer, employee, or agent of the State or political subdivision were taken in compliance with the detainer\u2014\n**(A)**\nthe officer, employee, or agent shall be deemed\u2014\n**(i)**\nto be an employee of the Federal Government and an investigative or law enforcement officer; and\n**(ii)**\nto have been acting within the scope of his or her employment under section 1346(b) and chapter 171 of title 28, United States Code;\n**(B)**\nsection 1346(b) of title 28, United States Code, shall provide the exclusive remedy for the plaintiff; and\n**(C)**\nthe United States shall be substituted as defendant in the proceeding.\n##### (c) Rule of construction\nNothing in this section may be construed to provide immunity to any person who knowingly violates the civil or constitutional rights of an individual.\n#### 3. Sanctuary jurisdiction defined\n##### (a) In general\nExcept as provided under subsection (b), for purposes of this Act, the term sanctuary jurisdiction means any State or political subdivision of a State that has in effect a statute, ordinance, policy, or practice that prohibits or restricts any government entity or official from\u2014\n**(1)**\nsending, receiving, maintaining, or exchanging with any Federal, State, or local government entity information regarding the citizenship or immigration status (lawful or unlawful) of any individual; or\n**(2)**\ncomplying with a request lawfully made by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act (8 U.S.C. 1226 and 1357) to comply with a detainer for, or notify about the release of, an individual.\n##### (b) Exception\nA State or political subdivision of a State shall not be deemed a sanctuary jurisdiction based solely on it having a policy whereby its officials will not share information regarding, or comply with a request made by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act (8 U.S.C. 1226 and 1357) to comply with a detainer regarding, an individual who comes forward as a victim or a witness to a criminal offense.\n#### 4. Sanctuary jurisdictions ineligible for certain Federal funds\n##### (a) Education grants\n**(1) National foundation on the arts and humanities grants**\nSection 7(f) of the National Foundation on the Arts and the Humanities Act of 1965 ( 20 U.S.C. 956(f) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking The Chairperson and inserting the following:\n(1) Except as provided in subparagraph (B), the Chairperson ;\n**(B)**\nby adding at the end the following:\n(B) (i) No application for a grant under this subsection may be approved unless the plan accompanying the application satisfies the requirements specified in this subsection. (ii) The Chairperson is not authorized to establish any grants-in-aid or allocate any Federal financial assistance or related Federal funding to a State or political subdivision of a State that is a sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). (iii) If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Chairperson or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Chairperson to withhold from such State any grant funding authorized under this section. ;\n**(C)**\nin paragraph (2)(A), by striking the undesignated matter at the end; and\n**(D)**\nin paragraph (3)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting No application may be approved by the Chairperson unless the accompanying plan satisfies the requirements specified in this subsection. after by the Chairperson. ; and\n**(ii)**\nby striking the undesignated matter at the end.\n**(2) National environmental education grants**\nSection 6(i) of the National Environmental Education Act ( 20 U.S.C. 5505(i) ) is amended\u2014\n**(A)**\nby striking Grants and inserting the following:\n(1) Maximum amount Grants ;\n**(B)**\nby striking In addition, 25 percent and inserting the following:\n(2) Set aside for small grants Not less than 25 percent ; and\n**(C)**\nby adding at the end the following:\n(3) Ineligibility of sanctuary jurisdictions The Administrator shall not provide any financial assistance under this section to any sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). (4) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Administrator or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Administrator to withhold from such State any financial assistance authorized under this section. .\n**(3) Elementary and secondary education grants**\nSection 1002 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6302 ) is amended\u2014\n**(A)**\nby redesignating subsection (f) as subsection (h); and\n**(B)**\nby inserting after subsection (e) the following:\n(f) Ineligibility for grants No appropriations authorized under this section for State and local educational agencies, education programs, or education services or assistance may be allocated as grants to any State or any political subdivision of a State that is a sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). (g) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Secretary or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Secretary to withhold from such State any funding appropriated pursuant to this section. .\n**(4) Higher education stem training grant program**\nSection 553 of the America COMPETES Reauthorization Act of 2010 ( 20 U.S.C. 9903 ) is amended by adding at the end the following:\n(h) Ineligibility for grants An institution of higher education located within a State or political subdivision of a State that is a sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ) is not eligible to receive a grant under this section. (i) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Director or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Director to withhold from such State any grant funding authorized under this section. .\n**(5) State fiscal stabilization education grants**\nSection 14001 of the American Recovery and Reinvestment Act of 2009 ( 20 U.S.C. 10001 ) is amended by adding at the end the following:\n(g) Ineligibility for grants The Secretary of Education shall not allocate any funds appropriated to carry out this title to any State or political subdivision of a State that is a sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). (h) Enforcement by the attorney general of a state If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Secretary or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Secretary to withhold from such State any grant funding allocated under this title. .\n##### (b) Grants for pollution research and pollution control programs\nThe Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. ) is amended\u2014\n**(1)**\nin section 104 ( 33 U.S.C. 1254 ), by adding at the end the following:\n(x) Ineligibility of sanctuary jurisdictions (1) In general The Administrator shall not make any grant under this section to any sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). (2) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Administrator or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Administrator to withhold from such State any grant funding authorized under this section. ; and\n**(2)**\nin section 106 ( 33 U.S.C. 1256 ), by\u2014\n**(A)**\nin subsection (d)\u2014\n**(i)**\nby striking No grant and inserting the following:\n(1) In general No grant ; and\n**(ii)**\nby adding at the end the following:\n(2) Ineligibility of sanctuary jurisdictions The Administrator shall not allot any funds appropriated pursuant to this section to any sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). ; and\n**(B)**\nadding at the end the following:\n(h) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Administrator or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Administrator to withhold from such State any allotment authorized under this section. .\n##### (c) Economic Development Administration grants\n**(1) Grants for public works and economic development**\nSection 201 of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3141(b) ) is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (2), by striking and at the end;\n**(ii)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(4) the area in which the project is to be carried out is not a sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). ; and\n**(B)**\nby adding at the end the following:\n(e) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Secretary or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Secretary to withhold from such State the grant funding authorized under this section. .\n**(2) Grants for planning and administrative expenses**\nSection 203(a) of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3143(a) ) is amended to read as follows:\n(a) In general (1) Grants authorized On the application of an eligible recipient, the Secretary may make grants to pay the costs of economic development planning and the administrative expenses of organizations that carry out such planning. (2) Ineligible recipients No State or political subdivision of a State shall be deemed an eligible recipient for purposes of grant funding under this section if it is a sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). (3) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Secretary or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Secretary to withhold from such State the grant funding authorized under this section. .\n**(3) Supplementary grants**\nSection 205 of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3145 ) is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (2), by striking and at the end;\n**(ii)**\nin paragraph (3)(B), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(4) will be carried out in a State that does not contain a sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). .\n**(B)**\nby adding at the end the following:\n(d) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Secretary or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Secretary to withhold from such State the supplementary grant funding authorized under this section. .\n**(4) Grants for training, research, and technical assistance**\nSection 207 of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3147 ) is amended by adding at the end the following:\n(d) Ineligibility of sanctuary jurisdictions Grant funds authorized under this section may not be used to provide assistance to any sanctuary jurisdiction (as defined in section 3 of the Sanctuary City Elimination Act ). (e) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Secretary or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Secretary to withhold from such State the grant funding authorized under this section. .\n##### (d) Community Development Block Grants\nTitle I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 102(a) ( 42 U.S.C. 5302(a) ), by adding at the end the following:\n(25) The term sanctuary jurisdiction has the meaning given such term in section 3 of the Sanctuary City Elimination Act . ;\n**(2)**\nin section 104(b) ( 42 U.S.C. 5304(b) )\u2014\n**(A)**\nin paragraph (5), by striking and at the end;\n**(B)**\nby redesignating paragraph (6) as paragraph (7); and\n**(C)**\nby inserting after paragraph (5) the following:\n(6) if the grantee is a State, a political subdivision of a State, or a unit of general local government, the grantee is not a sanctuary jurisdiction and will not become a sanctuary jurisdiction during the period for which the grantee receives a grant under this title; and ; and\n**(3)**\nin section 106 ( 42 U.S.C. 5306 ), by adding at the end the following:\n(g) Protection of individuals against crime (1) In general No funds authorized to be appropriated to carry out this title may be obligated or expended for any State, political subdivision of a State, or unit of general local government that is a sanctuary jurisdiction. (2) Returned amounts (A) State If a State or a political subdivision of a State is a sanctuary jurisdiction during the period for which it receives funding under this title, the Secretary\u2014 (i) shall direct the State or political subdivision to immediately return to the Secretary any such amounts that the State or political subdivision received for that period; and (ii) shall reallocate amounts returned under clause (i) for grants under this title to other States or political subdivisions of such States that are not sanctuary jurisdictions. (B) Unit of general local government If a unit of general local government is a sanctuary jurisdiction during the period for which it receives funding under this title, any such amounts that the unit of general local government received for that period\u2014 (i) in the case of a unit of general local government that is not in a nonentitlement area, shall be returned to the Secretary for grants under this title to States and other units of general local government that are not sanctuary jurisdictions; and (ii) in the case of a unit of general local government that is in a nonentitlement area, shall be returned to the Governor of the State for grants under this title to other units of general local government in the State that are not sanctuary jurisdictions. (C) Reallocation rules In reallocating amounts under subparagraphs (A) and (B), the Secretary\u2014 (i) shall apply the relevant allocation formula under subsection (b), with all sanctuary jurisdictions excluded; and (ii) shall not be subject to the rules for reallocation under subsection (c). (h) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Secretary or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Secretary to withhold from such State the funding authorized under this title. .\n##### (e) Brownfields Utilization, Investment, and Local Development Act of 2018 grant funding\nSection 104(k) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9604(k) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the paragraph heading, by striking Definition of eligible entity and inserting Definitions ;\n**(B)**\nby redesignating subparagraphs (A) through (L) as subclauses (I) through (XII), and by moving such clauses 4 ems to the right;\n**(C)**\nby striking In this subsection, the term eligible entity means\u2014 and inserting the following: \u201cIn this subsection:\n(A) Eligible entity The term eligible entity \u2014 (i) means\u2014 ; and\n**(D)**\nby adding at the end the following:\n(ii) does not include a sanctuary jurisdiction. (B) Sanctuary jurisdiction The term sanctuary jurisdiction has the meaning given such term in section 3 of the Sanctuary City Elimination Act . ;\n**(2)**\nby redesignating paragraphs (12) and (13) as paragraphs (13) and (14), respectively; and\n**(3)**\nby inserting after paragraph (11) the following:\n(12) Enforcement by the attorney general of a State If a State or a political subdivision of a State that is a sanctuary jurisdiction releases an alien from State or local custody and such alien subsequently commits any criminal offense (or admits to committing acts constituting the essential elements of any criminal offense) against any individual in any other State, the attorney general of the State in which such crime occurred shall have standing to bring an action against the Administrator or the State or political subdivision of such State that released such alien, on behalf of the injured party, in an appropriate district court of the United States to obtain injunctive relief requiring the Administrator to withhold from such State the grant funding and loans authorized under this subsection. .",
      "versionDate": "2026-04-16",
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
        "name": "Immigration",
        "updateDate": "2026-05-13T17:36:49Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4316is.xml"
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
      "title": "Sanctuary City Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T04:53:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sanctuary City Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure that State and local law enforcement may cooperate with Federal officials to protect our communities from violent criminals and suspected terrorists who are illegally present in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:48:57Z"
    }
  ]
}
```
