# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1680?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1680
- Title: UPLIFT Act
- Congress: 119
- Bill type: HR
- Bill number: 1680
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-01-07T19:26:17Z
- Update date including text: 2026-01-07T19:26:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1680",
    "number": "1680",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "UPLIFT Act",
    "type": "HR",
    "updateDate": "2026-01-07T19:26:17Z",
    "updateDateIncludingText": "2026-01-07T19:26:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:09:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1680ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1680\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Evans of Colorado (for himself, Mr. Crank , Ms. Boebert , and Mr. Hurd of Colorado ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 to expand the prohibition on State noncompliance with enforcement of the immigration laws, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unhandcuffing Police to Locate and Interdict Foreign Transgressors Act or the UPLIFT Act .\n#### 2. Purpose\nGiven recent infiltration of American communities by transnational criminal organizations such as Tren de Aragua, the Sinaloa Cartel, and MS\u201313 and the accompanying rise in crime that continue to impact American neighborhoods, the purposes of this act is to require law enforcement and other public servants in sanctuary jurisdictions to fully cooperate with the Departments of Justice and Homeland Security to protect American citizens and mitigate the flow of opioids, fentanyl, and other illicit drugs.\n#### 3. Noncompliance with enforcement of immigration law in sanctuary jurisdictions\n##### (a) In general\nSection 642 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1373 ) is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) In general Notwithstanding any other provision of Federal, State, or local law, no Federal, State, or local government entity, and no individual, may prohibit or in any way restrict, a Federal, State, or local government entity, official, or other personnel from complying with the immigration laws and policies of the United States or from assisting or cooperating with Federal law enforcement entities, officials, or other personnel regarding the enforcement of the immigration laws. ;\n**(2)**\nby amending subsection (b) to read as follows:\n(b) Law enforcement activities Notwithstanding any other provision of Federal, State, or local law, no Federal, State, or local government entity, and no individual, may prohibit, or in any way restrict, a Federal, State, or local government entity, official, or other personnel from undertaking any of the following law enforcement activities with respect to information regarding the citizenship or immigration status, lawful or unlawful, the inadmissibility or deportability, or the custody status, of any individual: (1) Making inquiries to any individual in order to obtain such information regarding such individual or any other individuals reasonably suspected of being involved in a crime. (2) Notifying the Federal Government regarding the presence of individuals reasonably suspected of being involved in a crime who are encountered by law enforcement officials or other personnel of a State or political subdivision of a State. (3) Complying with requests for such information from Federal law enforcement entities, officials, or other personnel. ;\n**(3)**\nin subsection (c), by striking Immigration and Naturalization Service and inserting Department of Homeland Security ;\n**(4)**\nby adding at the end the following:\n(d) Government Involvement in Immigration Detention Not withstanding any other provision of Federal, State, or local law, no Federal, State, or local government entity, and no individual, may in any way restrict a Federal, State, or local government entity, official, or other personnel from\u2014 (1) entering into an agreement for the detention of individuals in an immigration detention facility that is owned, managed, or operated by a private entity; (2) selling any government-owned property for the purpose of establishing an immigration detention facility that is or will be owned, managed, or operated by a private entity; (3) paying any costs related to the sale, purchase, construction, development, ownership, management, or operation of an immigration detention facility that is or will be owned, managed, or operated by a private entity; or (4) receiving any payment related to the detention of individuals in an immigration detention facility that is owned, managed, or operated by a private entity. (e) Standing for local jurisdictions To seek injunctive relief Any local government entity alleging a violation of subsection (a), (b), or (d) by the State in which the entity is located that harms such entity or its residents shall have standing to bring an action against the respective State on behalf of such entity or the residents of such entity in an appropriate district court of the United States to obtain appropriate injunctive relief. The court shall advance on the docket and expedite the disposition of a civil action filed under this subsection to the greatest extent practicable. For purposes of this subsection, local government entity or its residents shall be considered to have been harmed if the entity or any of its residents experience harm, including financial harm in excess of $100. (f) Compliance (1) Annual determination The Secretary of Homeland Security shall determine, for each calendar year, which States or local government entities are not in compliance with subsection (a) or (b) or (d) and shall report such determinations to Congress by March 1 of each succeeding calendar year. (2) Reports The Secretary shall issue a report concerning the compliance with subsections (a) and (b) of any particular State or local government entity at the request of the Committee on the Judiciary of the House of Representatives or the Committee on the Judiciary of the Senate. (g) Construction Nothing in this section shall require law enforcement officials from States, or from local government entities, to report or arrest victims of or witnesses to a criminal offense. .\n#### 4. Clarifying the authority of ice detainers\n##### (a) In general\nSection 287(d) of the Immigration and Nationality Act ( 8 U.S.C. 1357(d) ) is amended to read as follows:\n(d) Detainer of inadmissible or deportable aliens (1) In general In the case of an individual who is arrested by any Federal, State, or local law enforcement official or other personnel for the alleged violation of any criminal or motor vehicle law, the Secretary may issue a detainer regarding the individual to any Federal, State, or local law enforcement entity, official, or other personnel if the Secretary has probable cause to believe that the individual is an inadmissible or deportable alien. (2) Probable cause The Secretary may establish proabable cause if\u2014 (A) the individual who is the subject of the detainer matches, pursuant to biometric confirmation or other Federal database records, the identity of an alien who the Secretary has reasonable grounds to believe to be inadmissible or deportable; (B) the individual who is the subject of the detainer is the subject of ongoing removal proceedings, including matters where a charging document has already been served; (C) the individual who is the subject of the detainer has previously been ordered removed from the United States and such an order is administratively final; (D) the individual who is the subject of the detainer has made voluntary statements or provided reliable evidence that indicate that they are an inadmissible or deportable alien; or (E) the Secretary otherwise has probable cause to believe that the individual who is the subject of the detainer is an inadmissible or deportable alien. (3) Transfer of custody If the Federal, State, or local law enforcement entity, official, or other personnel to whom a detainer is issued complies with the detainer and detains the individual who is the subject of the detainer for purposes of transfer of custody to the Department of Homeland Security, the Department may take custody of the individual within 48 hours (excluding weekends and holidays), but in no instance more than 96 hours, following the date that the individual is otherwise to be released from the custody of the relevant Federal, State, or local law enforcement entity. .\n##### (b) Immunity; private right of action\nSection 287 of the Immigration and Nationality Act ( 8 U.S.C. 1357 ) is amended by adding at the end the following:\n(i) Immunity (1) In general A State or a political subdivision of a State (and the officials and personnel of the State or subdivision acting in their official capacities), and a nongovernmental entity (and its personnel) contracted by the State or political subdivision for the purpose of providing detention, acting in compliance with a Department of Homeland Security detainer issued pursuant to subsection (d), that temporarily holds an alien in its custody pursuant to the terms of such detainer so that the alien may be taken into the custody of the Department of Homeland Security, shall be considered to be acting under color of Federal authority for purposes of determining the liability, and immunity from suit, of the State or political subdivision of a State in a civil action brought under Federal or State law and shall not be liable for their compliance with the detainer in any suit seeking any punitive, compensatory, or other monetary damages. (2) Federal government as defendant In any civil action described in paragraph (1), the United States shall be the proper party named as the defendant in the action. (3) Bad faith exception Paragraphs (1) and (2) shall not apply to any mistreatment of an individual by a State or a political subdivision of a State (and the officials and personnel of the State or subdivision acting in their official capacities), or a nongovernmental entity (and its personnel) contracted by the State or political subdivision for the purpose of providing detention. (j) Private right of action (1) Cause of action Any individual, or a spouse, parent, or child of that individual (if the individual is deceased), who is the victim of a murder, rape, or any felony, under State or Federal law, for which an alien has been convicted and sentenced to a term of imprisonment of at least 1 year, may bring an action against a State or political subdivision of a State in the appropriate Federal or State court if the State or political subdivision released the alien from custody prior to the commission of such crime as a consequence of the State or political subdivision\u2019s declining to honor a detainer issued pursuant to subsection (d). (2) Limitation on bringing action An action brought under this subsection may not be brought later than 10 years following the date on which the crime was committed, or the date on which the victim died as a result of such crime, whichever occurs later. (3) Attorneys\u2019 fee and other costs In any action under this subsection the court shall award a prevailing plaintiff a reasonable attorneys\u2019 fee as part of the costs, and include expert fees as part of the attorneys\u2019 fee. .",
      "versionDate": "2025-02-27",
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
        "name": "Immigration",
        "updateDate": "2025-03-21T14:56:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
    "originChamber": "House",
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
          "measure-id": "id119hr1680",
          "measure-number": "1680",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2026-01-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1680v00",
            "update-date": "2026-01-07"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Unhandcuffing Police to Locate and Interdict Foreign Transgressors Act or the UPLIFT Act</strong></p><p>This bill requires additional cooperation from state and local governments in federal immigration enforcement.</p><p>Under current law, state and local governments are prohibited from implementing a ban on or in any way restricting the sharing of information regarding an individual\u2019s immigration status with federal agencies. The bill expands the prohibition to include any ban or restriction on complying with federal immigration laws or policies or on assisting or cooperating with federal law enforcement.</p><p>Additionally, state and local governments may not prohibit (1) inquiring about the immigration status of an individual who is suspected of involvement in a crime, (2) notifying the federal government of certain encounters, and (3) complying with federal requests for such information.</p><p>The bill also expands the standard for the issuance of a\u00a0detainer by the Department of Homeland Security (DHS). Under the bill, DHS may issue a detainer for an individual who is arrested on criminal charges or for a motor vehicle violation (currently, for drug violations) if DHS has probable cause that the individual is inadmissible or deportable. Probable cause may be established through methods including an identification match, voluntary statements made, or\u00a0through other means.</p><p>Federal immunity is also generally extended to state and local officials and government contractors who comply with a DHS detainer.</p><p>The bill also allows legal challenges against (1) state governments and local governments brought by certain crime victims, and (2) state governments brought by\u00a0local jurisdictions.\u00a0</p>"
        },
        "title": "UPLIFT Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1680.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Unhandcuffing Police to Locate and Interdict Foreign Transgressors Act or the UPLIFT Act</strong></p><p>This bill requires additional cooperation from state and local governments in federal immigration enforcement.</p><p>Under current law, state and local governments are prohibited from implementing a ban on or in any way restricting the sharing of information regarding an individual\u2019s immigration status with federal agencies. The bill expands the prohibition to include any ban or restriction on complying with federal immigration laws or policies or on assisting or cooperating with federal law enforcement.</p><p>Additionally, state and local governments may not prohibit (1) inquiring about the immigration status of an individual who is suspected of involvement in a crime, (2) notifying the federal government of certain encounters, and (3) complying with federal requests for such information.</p><p>The bill also expands the standard for the issuance of a\u00a0detainer by the Department of Homeland Security (DHS). Under the bill, DHS may issue a detainer for an individual who is arrested on criminal charges or for a motor vehicle violation (currently, for drug violations) if DHS has probable cause that the individual is inadmissible or deportable. Probable cause may be established through methods including an identification match, voluntary statements made, or\u00a0through other means.</p><p>Federal immunity is also generally extended to state and local officials and government contractors who comply with a DHS detainer.</p><p>The bill also allows legal challenges against (1) state governments and local governments brought by certain crime victims, and (2) state governments brought by\u00a0local jurisdictions.\u00a0</p>",
      "updateDate": "2026-01-07",
      "versionCode": "id119hr1680"
    },
    "title": "UPLIFT Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Unhandcuffing Police to Locate and Interdict Foreign Transgressors Act or the UPLIFT Act</strong></p><p>This bill requires additional cooperation from state and local governments in federal immigration enforcement.</p><p>Under current law, state and local governments are prohibited from implementing a ban on or in any way restricting the sharing of information regarding an individual\u2019s immigration status with federal agencies. The bill expands the prohibition to include any ban or restriction on complying with federal immigration laws or policies or on assisting or cooperating with federal law enforcement.</p><p>Additionally, state and local governments may not prohibit (1) inquiring about the immigration status of an individual who is suspected of involvement in a crime, (2) notifying the federal government of certain encounters, and (3) complying with federal requests for such information.</p><p>The bill also expands the standard for the issuance of a\u00a0detainer by the Department of Homeland Security (DHS). Under the bill, DHS may issue a detainer for an individual who is arrested on criminal charges or for a motor vehicle violation (currently, for drug violations) if DHS has probable cause that the individual is inadmissible or deportable. Probable cause may be established through methods including an identification match, voluntary statements made, or\u00a0through other means.</p><p>Federal immunity is also generally extended to state and local officials and government contractors who comply with a DHS detainer.</p><p>The bill also allows legal challenges against (1) state governments and local governments brought by certain crime victims, and (2) state governments brought by\u00a0local jurisdictions.\u00a0</p>",
      "updateDate": "2026-01-07",
      "versionCode": "id119hr1680"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1680ih.xml"
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
      "title": "UPLIFT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "UPLIFT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Unhandcuffing Police to Locate and Interdict Foreign Transgressors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 to expand the prohibition on State noncompliance with enforcement of the immigration laws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:30Z"
    }
  ]
}
```
