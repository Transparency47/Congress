# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8628?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8628
- Title: End U Visa Abuse Act
- Congress: 119
- Bill type: HR
- Bill number: 8628
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-22T10:23:36Z
- Update date including text: 2026-05-22T10:23:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8628",
    "number": "8628",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "End U Visa Abuse Act",
    "type": "HR",
    "updateDate": "2026-05-22T10:23:36Z",
    "updateDateIncludingText": "2026-05-22T10:23:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:00:40Z",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8628ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8628\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Roy (for himself, Mr. Self , and Mr. Crane ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo repeal section 101(a)(15)(U) of the Immigration and Nationality Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the End U Visa Abuse Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 2000, Congress established the U visa program with the intention of facilitating cooperation from alleged alien crime victims who might otherwise be reluctant to report crimes by deferring removal for foreign nationals, including illegal aliens, and providing work authorization and a pathway to lawful permanent status for U visa beneficiaries. Nearly all grounds of inadmissibility are waived for U visa applicants.\n**(2)**\nCongress imposed a cap of 10,000 U visas per year. U.S. Citizenship and Immigration Services created a waitlist that confers immigration benefits without any formal adjudication. Once waitlisted, aliens receive deferred action from removal and other immigration benefits. Additionally, there is no limit to derivative visas issued to qualifying family members.\n**(3)**\nAs of June 2025, there are over 400,000 U visa applications currently pending.\n**(4)**\nThe U visa program is rife with fraud and abuse and has demonstrated a record of illegal aliens using it to obtain lawful status and work permits to skirt deportation and removal, such as staging fake crimes and making false allegations to remain in the United States and possibly sponsor relatives who may also have unlawful status.\n**(5)**\nAccording to testimony submitted to the House Judiciary Committee\u2019s Subcommittee on Immigration, Integrity, Security, and Enforcement on June 25, 2025, U visa certifications are routinely rubberstamped, especially in sanctuary jurisdictions like California, where State laws like SB 674 pressure law enforcement agencies to certify U visas unless they affirmatively justify denial .\n**(6)**\nThe same testimony found The program allows any illegal alien to secretly accuse a U.S. citizen of a crime and apply for a visa after securing a law enforcement certification. No arrest. No charges. No conviction. Just an allegation\u2014often with no notice to the accused. The process is entirely ex parte, and there is no mechanism for rebuttal .\n**(7)**\nU.S. Citizenship and Immigration Services does not track the number of crimes solved through the issuance of a U visa.\n**(8)**\nAs an example of sweeping U visa fraud, on July 17, 2025, U.S. Citizenship and Immigration Services announced the indictment of 5 individuals, including 4 active and former law enforcement officers who were charged for bribery, conspiracy to commit visa fraud, and mail fraud, where charged individuals were accused of operating a 9-year scheme of fabricating fake crimes and police reports so aliens who were supposed victims could apply for U visas.\n**(9)**\nOn May 17, 2024, the Department of Justice announced the indictment of 6 individuals who allegedly conspired to stage armed robberies in Chicago and the suburbs so that purported victims could apply for U visas.\n**(10)**\nLocal law enforcement in Houston, Texas, uncovered a scheme that staged fake robberies at gunpoint for aliens to obtain U visas after a bystander reportedly shot and killed an individual who was pretending to be an armed robber who took the belongings of a couple at a gas station in January 2024, only to discover the purported thief and victims were staging a crime to garner a U visa.\n**(11)**\nIn March 2020, U.S. Citizenship and Immigration Services released a report examining U visa applications filed between 2012 and 2018, which found that only 5 percent of U visa petitioners reported having lawful immigration status at the time of application. 79 percent reported never having lawful status, and 14 percent said they were visa overstays.\n**(12)**\nThe March 2020 U.S. Citizenship and Immigration Services report also found that 10 percent of U visa recipients had committed immigration fraud, 8 percent reentered the United States illegally after removal, and 6 percent of those approved for the U visa had been ordered removed.\n**(13)**\nOn January 6, 2022, the Department of Homeland Security Office of Inspector General released a report entitled U.S. Citizenship and Immigration Services\u2019 U Visa Program Is Not Managed Effectively and Is Susceptible to Fraud . The report found that as part of the U visa process, applicants must submit the Form I\u2013918 Supplement B, U Nonimmigrant Status Certification, which includes a signature from an authorized agency or law enforcement official certifying the crime happened and attesting to the victim\u2019s cooperation. One of Office of Inspector General\u2019s findings was that it asked 125 law enforcement offices to confirm whether the signature on Supplement B forms certified by their office was that of an authorized signer . The Office of Inspector General found that at least 10 of the 125 U.S. Citizenship and Immigration Services-approved petitions had forged, unauthorized, altered, or suspicious law enforcement certifications .\n**(14)**\nAdditionally, the Office of Inspector General found that U.S. Citizenship and Immigration Services did not implement its recommendations regarding fraud in the program.\n**(15)**\nAs of April 10, 2026, 10 foreign nationals were indicted for visa fraud conspiracy for allegedly carrying out staged armed robberies of convenience store clerks so they could falsely claim a U visa to remain in the country.\n**(16)**\nVictimization should not be a basis for an immigration benefit. If an alien is a crime victim and is actively cooperating with law enforcement as a witness, the S visa is already available and should be utilized if needed, alternatively, the Department of Homeland Security Secretary can grant humanitarian immigration parole to purported alien crime victims or witnesses on a case-by-case basis if they are needed by law enforcement or are required to testify.\n**(17)**\nCongress should repeal the U visa program in full, as it no longer serves a valid purpose and encourages fraud, rewarding illegal aliens who commit it with the likelihood of a green card and work permit, further enabling lawlessness and illegal immigration, leaving law-abiding American citizens and legal immigrants to deal with the consequences.\n#### 3. Repeal of U Visa program\n##### (a) Repeal\nSubparagraph (U) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) is repealed.\n##### (b) Conforming amendments\nThe Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended\u2014\n**(1)**\nin section 204\u2014\n**(A)**\nin subsection (a)(1)(L), by striking or (U) ; and\n**(B)**\nin subsection (l)(2)(E), by striking or in U nonimmigrant status as described in section 101(a)(15)(U)(ii) ;\n**(2)**\nin section 212\u2014\n**(A)**\nin subsection (a)(4)(E)\u2014\n**(i)**\nby striking clause (ii); and\n**(ii)**\nredesignating clause (iii) as clause (ii); and\n**(B)**\nin subsection (d), by striking paragraph (14);\n**(3)**\nin section 214, by striking subsection (p);\n**(4)**\nin section 237(d)(1), by striking or (U) each place it appears;\n**(5)**\nin section 239(e)(2)(B), by striking or (U) ;\n**(6)**\nin section 245\u2014\n**(A)**\nin subsection (l)(7), by striking 101(a)(15)(U), ; and\n**(B)**\nby striking subsection (m); and\n**(7)**\nin section 248(b), by striking or (U) .",
      "versionDate": "2026-04-30",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8628ih.xml"
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
      "title": "End U Visa Abuse Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End U Visa Abuse Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal section 101(a)(15)(U) of the Immigration and Nationality Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:30Z"
    }
  ]
}
```
